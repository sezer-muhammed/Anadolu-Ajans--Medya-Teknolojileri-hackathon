from django import forms
from api.models import ImageUpload, TextUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = TextUpload
        fields = ['text']
