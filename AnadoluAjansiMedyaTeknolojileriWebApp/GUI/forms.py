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

from image_generator.models import *



class ImageGenerationSearchForm(forms.Form):
    # NewsContext fields
    headline = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Headline'}))
    category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Category'}))
    emotional_intensity = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Emotional Intensity'}))
    geographical_context = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Geographical Context'}))
    temporal_context = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Temporal Context'}))
    source_credibility = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Source Credibility'}))
    audience_age_group = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Audience Age Group'}))
    audience_interests = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Audience Interests', 'rows': 3}))
    keywords = forms.ModelMultipleChoiceField(queryset=Keyword.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select mb-3 select2', 'multiple': 'multiple'}))
    subcategories = forms.ModelMultipleChoiceField(queryset=Subcategory.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select mb-3 select2', 'multiple': 'multiple'}))

    # VisualElements fields
    main_subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Main Subject'}))
    background_scene = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Background Scene'}))
    color_palette = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Color Palette'}))
    texture = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Texture'}))
    characters = forms.ModelMultipleChoiceField(queryset=Character.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select mb-3 select2', 'multiple': 'multiple'}))
    object_details = forms.ModelMultipleChoiceField(queryset=ObjectDetail.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'form-select mb-3 select2', 'multiple': 'multiple'}))

    # StylePreferences fields
    art_style = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Art Style'}))
    composition = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Composition'}))
    lighting = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lighting'}))
    aspect_ratio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Aspect Ratio'}))

    # UserCustomizations fields
    additional_text = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Additional Text', 'rows': 3}))
    user_uploads = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'User Uploads', 'rows': 3}))
    specific_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Specific Requests', 'rows': 3}))
    feedback_loop = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Feedback Loop', 'rows': 3}))
    templates = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Templates', 'rows': 3}))
