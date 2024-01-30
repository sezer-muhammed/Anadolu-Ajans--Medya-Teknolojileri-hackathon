from django.contrib import admin
from .models import ImageUpload, TextUpload, VoiceUpload
from django.utils.html import mark_safe

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ["id", "display_image", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["id", "created_at"]

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="150" />')
        return "No image"
    display_image.short_description = "Image"
    display_image.allow_tags = True

@admin.register(TextUpload)
class TextUploadAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["text", "created_at"]


@admin.register(VoiceUpload)
class VoiceUploadAdmin(admin.ModelAdmin):
    list_display = ["id", "voice_file"]
    list_filter = ["id"]
    search_fields = ["id"]
