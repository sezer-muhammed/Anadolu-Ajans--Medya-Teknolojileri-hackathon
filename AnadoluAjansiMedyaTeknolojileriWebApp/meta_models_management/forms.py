from django import forms
from api.models import ImageUpload, TextUpload, VoiceUpload

from .models import (
    Keyword, AssociatedEmotion, Object, TextExtraction, 
    SourceAttribute, ContentTheme, Audience, GeographicRelevance, 
    TemporalRelevance, TechnicalLevel, SentimentTrend, InfluencerTag,
    SourceInfo, ContentAnalysis, EmotionAnalysis, AIDetection, 
    AdditionalMetadata, InputRecord
)

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


class SearchForm(forms.Form):
    # Fields from InputRecord
    input_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Input ID'}))
    input_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Input Type'}))
    timestamp = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Timestamp'}))
    
    # Fields from related models (as examples)
    keyword = forms.ModelChoiceField(queryset=Keyword.objects.all(), required=False)
    emotion = forms.ModelChoiceField(queryset=AssociatedEmotion.objects.all(), required=False)
    object_name = forms.ModelChoiceField(queryset=Object.objects.all(), required=False)
    text_extraction = forms.ModelChoiceField(queryset=TextExtraction.objects.all(), required=False)
    source_attribute = forms.ModelChoiceField(queryset=SourceAttribute.objects.all(), required=False)
    content_theme = forms.ModelChoiceField(queryset=ContentTheme.objects.all(), required=False)
    audience_type = forms.ModelChoiceField(queryset=Audience.objects.all(), required=False)
    geographic_relevance = forms.ModelChoiceField(queryset=GeographicRelevance.objects.all(), required=False)
    temporal_relevance = forms.ModelChoiceField(queryset=TemporalRelevance.objects.all(), required=False)
    technical_level = forms.ModelChoiceField(queryset=TechnicalLevel.objects.all(), required=False)
    sentiment_trend = forms.ModelChoiceField(queryset=SentimentTrend.objects.all(), required=False)
    influencer_tag = forms.ModelChoiceField(queryset=InfluencerTag.objects.all(), required=False)

    # You can add as many fields as you want from related models.
    # Note: If the related fields have many possible values, you might want to use AJAX to load options dynamically.