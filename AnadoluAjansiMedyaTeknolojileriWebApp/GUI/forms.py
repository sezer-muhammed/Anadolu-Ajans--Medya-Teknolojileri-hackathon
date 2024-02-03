from django import forms
from api.models import ImageUpload, TextUpload
from image_generator.models import *
from django_select2 import forms as s2forms
from django.db.models.functions import Coalesce
from django.db.models import F

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = TextUpload
        fields = ['text']

class ImageGenerationSelectForm(forms.Form):
    image_generation = forms.ModelChoiceField(
        queryset=ImageGeneration.objects.filter(
            text_upload__isnull=False
        ).annotate(
            sort_date=F('text_upload__created_at')
        ).order_by('-sort_date'),
        label="Select a News Context",
        widget=s2forms.Select2Widget(attrs={
            'data-placeholder': 'Select Headlines', 
            'data-allow-clear': True,
            'class': 'select2-large',  # Modified class name for larger size
            'style': 'width: 100%;'  # Ensure the select box takes full width
        })
    )

    def __init__(self, *args, **kwargs):
        super(ImageGenerationSelectForm, self).__init__(*args, **kwargs)
        self.fields['image_generation'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        # Customizing the display of each dropdown item with more details
        return f"{obj.news_context.headline} - {obj.news_context.category} - {obj.news_context.emotionTone} - {obj.text_upload.created_at.strftime('%Y-%m-%d')}"



class ImageGenerationSearchForm(forms.Form):
    headline = forms.ModelMultipleChoiceField(
        queryset=NewsContext.objects.all(),
        required=False,
        widget=s2forms.Select2MultipleWidget(attrs={
            'data-placeholder': 'Select Headlines', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )

    keywords = forms.ModelMultipleChoiceField(
        queryset=Keyword.objects.all(),
        required=False,
        widget=s2forms.Select2MultipleWidget(attrs={
            'data-placeholder': 'Select Keywords', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )

    subcategories = forms.ModelMultipleChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,
        widget=s2forms.Select2MultipleWidget(attrs={
            'data-placeholder': 'Select Subcategories', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )

    object_details = forms.ModelMultipleChoiceField(
        queryset=ObjectDetail.objects.all(),
        required=False,
        widget=s2forms.Select2MultipleWidget(attrs={
            'data-placeholder': 'Select Object Details', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )

    characters = forms.ModelMultipleChoiceField(
        queryset=Character.objects.all(),
        required=False,
        widget=s2forms.Select2MultipleWidget(attrs={
            'data-placeholder': 'Select Characters', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )


    has_text_upload = forms.BooleanField(
        required=False, 
        label='Has Text Upload',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    has_image_upload = forms.BooleanField(
        required=False, 
        label='Has Image Upload',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )