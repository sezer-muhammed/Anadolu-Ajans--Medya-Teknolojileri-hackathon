from django import forms
from api.models import ImageUpload, TextUpload, VoiceUpload
from django_select2 import forms as s2forms
from django_select2.forms import Select2MultipleWidget, Select2Widget

from .models import (
    Keyword,
    AssociatedEmotion,
    Object,
    TextExtraction,
    SourceAttribute,
    ContentTheme,
    Audience,
    GeographicRelevance,
    TemporalRelevance,
    TechnicalLevel,
    SentimentTrend,
    InfluencerTag,
    SourceInfo,
    ContentAnalysis,
    EmotionAnalysis,
    AIDetection,
    AdditionalMetadata,
    InputRecord,
)


class CombinedUploadForm(forms.ModelForm):
    """
    A form for handling the combined upload of images, texts, and voice files.

    This form allows for the upload of multiple files and text blocks, handling each
    type of media differently. Images and voices are uploaded as files, while texts
    are input as character fields.

    Attributes
    ----------
    images : FileField
        A field for uploading multiple image files. Not required.
    texts : CharField
        A field for inputting text. Text blocks are split by double new lines. Not required.
    voices : FileField
        A field for uploading multiple voice files. Not required.

    Methods
    -------
    save(commit=True):
        Saves the uploaded files and texts to their respective models. Handles custom
        saving logic for multiple files and text blocks.

    Notes
    -----
    The actual saving to the database is handled in the custom `save` method, which
    needs to be called explicitly after form validation.
    """

    images = forms.FileField(widget=forms.FileInput(), required=False)
    texts = forms.CharField(widget=forms.Textarea, required=False)
    voices = forms.FileField(widget=forms.FileInput(), required=False)

    class Meta:
        model = ImageUpload  # Just a placeholder, actual save will be custom
        fields = []

    def save(self, commit=True):
        """
        Saves the uploaded files and texts to their respective models.

        Parameters
        ----------
        commit : bool, optional
            Whether to commit the save to the database immediately. Default is True.

        Returns
        -------
        object
            The instance of the form's model with the uploaded data saved.

        Raises
        ------
        ValidationError
            If the form is invalid.

        Notes
        -----
        This method handles custom saving logic for multiple files and text blocks.
        Images are saved to the ImageUpload model, texts to the TextUpload model,
        and voices to the VoiceUpload model. Texts are split by double new lines
        and each non-whitespace block is saved separately.
        """
        # Custom save method to handle multiple files and texts
        images = self.files.getlist("images")
        texts = self.cleaned_data.get("texts")
        voices = self.files.getlist("voices")

        # Save images
        for image in images:
            ImageUpload.objects.create(image=image)

        # Save texts, split by double new lines
        if texts:
            text_blocks = texts.split("\n\n")
            for text in text_blocks:
                if text.strip():  # Checking if the text is not just whitespace
                    TextUpload.objects.create(text=text.strip())

        # Save voices
        for voice in voices:
            VoiceUpload.objects.create(voice_file=voice)

        return super().save(commit)


class SearchForm(forms.Form):
    """
    A form for conducting complex searches across various related models.

    This form allows for querying a database using various criteria from different models,
    enabling a detailed and refined search process.

    Attributes
    ----------
    input_id : CharField
        Field for querying by Input ID. Optional.
    input_type : CharField
        Field for querying by Input Type. Optional.
    timestamp : CharField
        Field for querying by Timestamp. Optional.
    keyword : ModelChoiceField
        Dropdown for selecting a keyword. Optional.
    emotion : ModelChoiceField
        Dropdown for selecting an associated emotion. Optional.
    object_name : ModelChoiceField
        Dropdown for selecting an object. Optional.
    text_extraction : ModelChoiceField
        Dropdown for selecting text extraction. Optional.
    source_attribute : ModelChoiceField
        Dropdown for selecting a source attribute. Optional.
    content_theme : ModelChoiceField
        Dropdown for selecting a content theme. Optional.
    audience_type : ModelChoiceField
        Dropdown for selecting an audience type. Optional.
    geographic_relevance : ModelChoiceField
        Dropdown for selecting geographic relevance. Optional.
    temporal_relevance : ModelChoiceField
        Dropdown for selecting temporal relevance. Optional.
    technical_level : ModelChoiceField
        Dropdown for selecting a technical level. Optional.
    sentiment_trend : ModelChoiceField
        Dropdown for selecting a sentiment trend. Optional.
    influencer_tag : ModelChoiceField
        Dropdown for selecting an influencer tag. Optional.

    Notes
    -----
    This form does not directly interact with any specific database model but is
    designed to facilitate searching across multiple related models. The fields
    are meant to correspond with various attributes of the records in the database,
    allowing for a multifaceted search.
    """

    # Fields from InputRecord
    input_id = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Input ID"})
    )
    input_type = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Input Type"})
    )
    timestamp = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Timestamp"})
    )

    # Fields from related models (as examples)
    keyword = forms.ModelMultipleChoiceField(
        queryset=Keyword.objects.all(), 
        required=False,
        widget=s2forms.Select2MultipleWidget
    )
    emotion = forms.ModelMultipleChoiceField(
        queryset=AssociatedEmotion.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    object_name = forms.ModelMultipleChoiceField(queryset=Object.objects.all(), required=False, widget=s2forms.Select2MultipleWidget)
    text_extraction = forms.ModelMultipleChoiceField(
        queryset=TextExtraction.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    source_attribute = forms.ModelMultipleChoiceField(
        queryset=SourceAttribute.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    content_theme = forms.ModelMultipleChoiceField(
        queryset=ContentTheme.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    audience_type = forms.ModelMultipleChoiceField(
        queryset=Audience.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    geographic_relevance = forms.ModelMultipleChoiceField(
        queryset=GeographicRelevance.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    temporal_relevance = forms.ModelMultipleChoiceField(
        queryset=TemporalRelevance.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    technical_level = forms.ModelMultipleChoiceField(
        queryset=TechnicalLevel.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    sentiment_trend = forms.ModelMultipleChoiceField(
        queryset=SentimentTrend.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )
    influencer_tag = forms.ModelMultipleChoiceField(
        queryset=InfluencerTag.objects.all(), required=False, widget=s2forms.Select2MultipleWidget
    )

    # You can add as many fields as you want from related models.
    # Note: If the related fields have many possible values, you might want to use AJAX to load options dynamically.
