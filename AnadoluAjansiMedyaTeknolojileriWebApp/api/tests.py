from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import ImageUpload, TextUpload, VoiceUpload

class ImageUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        # Set up any initial data or settings you need for the tests
        self.image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        self.url = '/images/'

    def test_create_image(self):
        # Test creating an image through the API
        response = self.client.post(self.url, {'image': self.image})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ImageUpload.objects.count(), 1)

    def test_retrieve_images(self):
        # Test retrieving images through the API
        self.client.post(self.url, {'image': self.image})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TextUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.text = 'Sample text'
        self.url = '/api/texts/'

    def test_create_text(self):
        response = self.client.post(self.url, {'text': self.text})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TextUpload.objects.count(), 1)

    def test_retrieve_texts(self):
        self.client.post(self.url, {'text': self.text})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class VoiceUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.voice_file = SimpleUploadedFile(name='test_voice.mp3', content=b'Some audio content', content_type='audio/mpeg')
        self.url = '/voices/'

    def test_create_voice(self):
        response = self.client.post(self.url, {'voice_file': self.voice_file})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VoiceUpload.objects.count(), 1)

    def test_retrieve_voices(self):
        self.client.post(self.url, {'voice_file': self.voice_file})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

