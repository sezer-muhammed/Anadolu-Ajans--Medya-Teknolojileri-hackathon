from django.views import View
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageUploadForm, TextUploadForm, ImageGenerationSearchForm
from api.models import TextUpload, ImageUpload
from django.http import HttpResponse
import json
from io import BytesIO
from django.core.files.images import ImageFile
from django.views.generic.list import ListView
from image_generator.models import ImageGeneration, GeneratedImages, Keyword
from image_generator.serializers import ImageGenerationSerializer
import requests
from .openai_interface import OpenAIInterface
from django.db.models import Case, When, Value, F
from django.db.models.functions import Coalesce
from .config.openai_prompt import TEXT_PROMPT

def text2img(params: dict) -> dict:
    """
    text to image
    """
    host = "http://127.0.0.1:8888"
    result = requests.post(url=f"{host}/v1/generation/text-to-image",
                           data=json.dumps(params),
                           headers={"Content-Type": "application/json"})
    return result.json()

class GenerateImagesView(View):
    def get(self, request, pk):
        try:
            image_generation = ImageGeneration.objects.get(pk=pk)
        except ImageGeneration.DoesNotExist:
            return HttpResponse(f"ImageGeneration object with id {pk} does not exist.", status=404)

        # Serialize the object
        serializer = ImageGenerationSerializer(image_generation)

        # Convert to Python data structure
        data = serializer.data

        # Remove 'image_upload' and 'text_upload' fields
        data.pop('image_upload', None)
        data.pop('text_upload', None)
        with open("GUI/config/structure.json", 'r') as file:
            data_template = json.load(file)

        chatgpt_interface = OpenAIInterface()

        # Convert the data to a formatted string
        formatted_json_str = json.dumps(data_template, indent=4)
        # Convert to JSON string with formatting
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        prompt = TEXT_PROMPT.format(data=formatted_json_str, text=json_data)
        result_prompt_for_image_generation = chatgpt_interface.generate_text(prompt)

        result =text2img(result_prompt_for_image_generation)

        for image_data in result:
            image_url = image_data['url']

            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                # Create a Django File object
                image_name = image_url.split('/')[-1]  # Extracting the name of the file
                image_file = ImageFile(BytesIO(response.content), name=image_name)

                # Create and save the GeneratedImages object
                generated_image = GeneratedImages(image=image_file, image_generation=image_generation)
                generated_image.save()
        return redirect('imagegeneration_detail', pk=pk)

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
    template_name = 'GUI/image_generation_list.html'
    context_object_name = 'image_generations'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            sort_date=Coalesce(
                'text_upload__created_at',
                'image_upload__created_at'
            )
        ).order_by('-sort_date')
        form = ImageGenerationSearchForm(self.request.GET)
        if form.is_valid():
            headlines = form.cleaned_data.get('headline')
            keywords = form.cleaned_data.get('keywords')
            subcategories = form.cleaned_data.get('subcategories')
            object_details = form.cleaned_data.get('object_details')
            characters = form.cleaned_data.get('characters')
            has_text_upload = form.cleaned_data.get('has_text_upload')
            has_image_upload = form.cleaned_data.get('has_image_upload')

            if headlines:
                queryset = queryset.filter(news_context__in=headlines)

            if keywords:
                queryset = queryset.filter(news_context__keywords__in=keywords).distinct()

            if subcategories:
                queryset = queryset.filter(news_context__subcategories__in=subcategories).distinct()

            if object_details:
                queryset = queryset.filter(visual_elements__object_details__in=object_details).distinct()

            if characters:
                queryset = queryset.filter(visual_elements__characters__in=characters).distinct()

            if has_text_upload:
                queryset = queryset.exclude(text_upload__isnull=True)

            if has_image_upload:
                queryset = queryset.exclude(image_upload__isnull=True)

            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ImageGenerationSearchForm(self.request.GET or None)  # Initialize the form
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
