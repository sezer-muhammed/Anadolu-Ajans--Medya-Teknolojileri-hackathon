from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm, TextUploadForm
from api.models import TextUpload, ImageUpload
from django.http import HttpResponse

from django.views.generic.list import ListView
from image_generator.models import ImageGeneration, GeneratedImages

class GenerateImagesView(View):
    def get(self, request, pk):
        # Placeholder for actual image generation implementation
        # You would trigger the image generation process here and then redirect or update the response
        return HttpResponse(f"Generate images for ImageGeneration with id {pk}")

class ImageGenerationDetailView(View):
    def get(self, request, pk):
        # Retrieve the ImageGeneration instance using pk
        image_generation = get_object_or_404(ImageGeneration, pk=pk)

        # Check if either image_upload or text_upload is not null or empty
        if image_generation.image_upload:
            upload_info = image_generation.image_upload.image.url
        elif image_generation.text_upload:
            upload_info = image_generation.text_upload.text
        else:
            upload_info = "No additional uploads provided."

        # Retrieve all images associated with the ImageGeneration
        generated_images = GeneratedImages.objects.filter(image_generation=image_generation)

        # Render the template with the data
        return render(request, 'GUI/image_generation_detail.html', {
            'image_generation': image_generation,
            'upload_info': upload_info,
            'generated_images': generated_images,
        })

class ImageGenerationListView(ListView):
    model = ImageGeneration
    template_name = 'GUI/image_generation_list.html'  # Your template name
    context_object_name = 'image_generations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context if necessary
        return context


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
