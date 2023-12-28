from django.contrib import admin
from .models import ImageUpload, TextUpload, VoiceUpload

# Register your models here.
@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_filter = ['id']
    search_fields = ['id']

@admin.register(TextUpload)
class TextUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_filter = ['id']
    search_fields = ['text']

@admin.register(VoiceUpload)
class VoiceUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'voice_file']
    list_filter = ['id']
    search_fields = ['id']
