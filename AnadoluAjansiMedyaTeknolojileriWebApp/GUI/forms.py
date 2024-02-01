from django import forms
from api.models import ImageUpload, TextUpload
from image_generator.models import *
from django_select2 import forms as s2forms

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
        queryset=ImageGeneration.objects.all(),
        label="Select an News Context",
        widget=s2forms.Select2Widget(attrs={
            'data-placeholder': 'Select Headlines', 
            'data-allow-clear': True,
            'class': 'select2'
        })
    )


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