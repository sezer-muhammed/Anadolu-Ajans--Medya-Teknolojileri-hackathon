from django.views import View
from django.shortcuts import render, redirect
from .forms import ImageUploadForm, TextUploadForm
from api.models import TextUpload, ImageUpload

class MediaUploadView(View):
    def get(self, request, *args, **kwargs):
        image_form = ImageUploadForm()
        text_form = TextUploadForm()
        return render(request, 'GUI/upload_media.html', {
            'image_form': image_form,
            'text_form': text_form
        })

    def post(self, request, *args, **kwargs):
        image_form = ImageUploadForm(request.POST, request.FILES)
        text_form = TextUploadForm(request.POST)

        if image_form.is_valid():
            for file in request.FILES.getlist('image'):
                ImageUpload.objects.create(image=file)

        if text_form.is_valid():
            # Split the text by '%%' and save each as a separate entry
            texts = text_form.cleaned_data['text'].split('%%')
            for text in texts:
                TextUpload.objects.create(text=text.strip())

        return redirect('/GUI/upload')
