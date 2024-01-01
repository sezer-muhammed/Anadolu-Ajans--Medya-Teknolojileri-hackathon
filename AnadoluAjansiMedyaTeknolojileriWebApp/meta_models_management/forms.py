from django import forms
from api.models import ImageUpload, TextUpload, VoiceUpload

class CombinedUploadForm(forms.ModelForm):
    images = forms.FileField(widget=forms.FileInput(), required=False)
    texts = forms.CharField(widget=forms.Textarea, required=False)
    voices = forms.FileField(widget=forms.FileInput(), required=False)

    class Meta:
        model = ImageUpload  # Just a placeholder, actual save will be custom
        fields = []

    def save(self, commit=True):
        # Custom save method to handle multiple files and texts
        images = self.files.getlist('images')
        texts = self.cleaned_data.get('texts')
        voices = self.files.getlist('voices')

        # Save images
        for image in images:
            ImageUpload.objects.create(image=image)

        # Save texts, split by double new lines
        if texts:
            text_blocks = texts.split('\n\n')
            for text in text_blocks:
                if text.strip():  # Checking if the text is not just whitespace
                    TextUpload.objects.create(text=text.strip())

        # Save voices
        for voice in voices:
            VoiceUpload.objects.create(voice_file=voice)

        return super().save(commit)
