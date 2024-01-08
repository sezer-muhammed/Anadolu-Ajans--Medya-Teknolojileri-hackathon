import os
import glob
from django.core.files import File  # Import the File class
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from faker import Faker

from .models import ImageUpload, TextUpload, VoiceUpload


class ImageUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        # Define the path to your sample image
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "api", "test_media", "base_test_image.jpg")

        # Open the sample image and read it
        with open(image_path, "rb") as image_file:
            image = File(image_file)
            self.image = SimpleUploadedFile(
                name="test_image.jpg",
                content=image_file.read(),
                content_type="image/jpeg",
            )

        self.url = "/api/images/"

    def test_create_image(self):
        # Test creating an image through the API
        response = self.client.post(self.url, {"image": self.image})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ImageUpload.objects.count(), 1)

    def test_retrieve_images(self):
        # Test retrieving images through the API
        self.client.post(self.url, {"image": self.image})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        # Define the path to your media/images folder
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_image_path = os.path.join(base_dir, "media", "images")

        # Pattern to match all files starting with 'test_' in the media/images directory
        test_files_pattern = os.path.join(media_image_path, "test_*")

        # Use glob to find all matching files
        test_files = glob.glob(test_files_pattern)

        # Remove each file
        for file in test_files:
            os.remove(file)

        super().tearDown()  # Call the tearDown method of the superclass.


class TextUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        self.text = "Sample text"
        self.url = "/api/texts/"

    def test_create_text(self):
        response = self.client.post(self.url, {"text": self.text})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TextUpload.objects.count(), 1)

    def test_retrieve_texts(self):
        self.client.post(self.url, {"text": self.text})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class VoiceUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        # Initialize Faker
        self.fake = Faker()

        self.voice_file = SimpleUploadedFile(
            name="test_voice.mp3",
            content=b"Some audio content",
            content_type="audio/mpeg",
        )
        self.url = "/api/voices/"

    def test_create_voice(self):
        # Use Faker to generate random text
        fake_transcript = self.fake.paragraph(nb_sentences=5)

        response = self.client.post(
            self.url, {"voice_file": self.voice_file, "transcript": fake_transcript}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VoiceUpload.objects.count(), 1)

        voice_upload = VoiceUpload.objects.first()

        self.assertEqual(
            voice_upload.transcript, fake_transcript
        )  # Check if the transcript matches the fake one

    def test_retrieve_voices(self):
        fake_transcript = self.fake.paragraph(nb_sentences=5)
        self.client.post(
            self.url, {"voice_file": self.voice_file, "transcript": fake_transcript}
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        # Define the path to your media/images folder
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_image_path = os.path.join(base_dir, "media", "voices")

        # Pattern to match all files starting with 'test_' in the media/images directory
        test_files_pattern = os.path.join(media_image_path, "test_*")

        # Use glob to find all matching files
        test_files = glob.glob(test_files_pattern)

        # Remove each file
        for file in test_files:
            os.remove(file)

        super().tearDown()  # Call the tearDown method of the superclass.
