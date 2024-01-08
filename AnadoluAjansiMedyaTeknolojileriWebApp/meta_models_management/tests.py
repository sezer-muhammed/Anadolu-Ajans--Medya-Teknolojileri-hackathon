from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import InputRecordSerializer
from faker import Faker
import json
import os
from datetime import datetime
from django.conf import settings


class InputRecordSerializerTestCase(TestCase):
    """
    Test cases for serialization and deserialization of InputRecord instances.

    This class contains setup for creating a user and various related objects for testing,
    as well as test cases for saving, retrieving, and interacting with InputRecord instances via the API.
    """

    def setUp(self):
        """
        Set up the test environment by creating a user, related objects, and an InputRecord instance.

        This method runs before every individual test. It sets up a user for authentication,
        creates various related objects such as Location, SourceInfo, ContentAnalysis, and others,
        and finally creates an InputRecord instance with all the related objects linked.
        """
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        self.faker = Faker()

        # Create related objects
        # Location
        location = SourceLocation.objects.create(
            latitude=float(self.faker.latitude()),
            longitude=float(self.faker.longitude()),
        )

        # SourceInfo
        source_info = SourceInfo.objects.create(
            source=self.faker.company(),
            city=self.faker.city(),
            country=self.faker.country(),
            location=location,
        )

        # ContentAnalysis
        content_analysis = ContentAnalysis.objects.create(
            detailed_description=self.faker.text(), summary=self.faker.sentence()
        )
        for _ in range(500):
            keyword = Keyword.objects.create(value=self.faker.word())
            content_analysis.keywords.add(keyword)
            content_analysis.keywords.add(keyword)

        # EmotionAnalysis
        emotion_analysis = EmotionAnalysis.objects.create()
        for _ in range(120):
            emotion = AssociatedEmotion.objects.create(emotion=self.faker.word())
            emotion_analysis.associated_emotions.add(emotion)
            emotion_analysis.associated_emotions.add(emotion)

        # AIDetection
        ai_detection = AIDetection.objects.create(emotion_analysis=emotion_analysis)
        for _ in range(120):
            obj = Object.objects.create(
                name=self.faker.word(),
                status=self.faker.word(),
                action=self.faker.word(),
            )
            ai_detection.object_detection.add(obj)
            ai_detection.object_detection.add(obj)
        for _ in range(120):
            text = TextExtraction.objects.create(text=self.faker.sentence())
            ai_detection.text_extraction.add(text)
            ai_detection.text_extraction.add(text)

        # AdditionalMetadata
        additional_metadata = AdditionalMetadata.objects.create()

        for _ in range(120):
            attribute = SourceAttribute.objects.create(attribute=self.faker.word())
            additional_metadata.source_attributes.add(attribute)
            additional_metadata.source_attributes.add(attribute)

        for _ in range(120):
            theme = ContentTheme.objects.create(theme=self.faker.word())
            additional_metadata.content_themes.add(theme)
            additional_metadata.content_themes.add(theme)

        for _ in range(120):
            audience_type = Audience.objects.create(audience_type=self.faker.word())
            additional_metadata.audience.add(audience_type)

        for _ in range(120):
            geography = GeographicRelevance.objects.create(geography=self.faker.word())
            additional_metadata.geographic_relevance.add(geography)

        for _ in range(120):
            temporal = TemporalRelevance.objects.create(temporal=self.faker.date())
            additional_metadata.temporal_relevance.add(temporal)

        for _ in range(120):
            level = TechnicalLevel.objects.create(level=self.faker.word())
            additional_metadata.technical_level.add(level)

        for _ in range(120):
            trend = SentimentTrend.objects.create(trend=self.faker.word())
            additional_metadata.sentiment_trends.add(trend)

        for _ in range(120):
            tag = InfluencerTag.objects.create(tag=self.faker.word())
            additional_metadata.influencer_tags.add(tag)

        # InputRecord setup
        self.input_record = InputRecord.objects.create(
            input_id=self.faker.uuid4(),
            input_type=self.faker.word(),
            timestamp=self.faker.iso8601(),
            source_info=source_info,
            content_analysis=content_analysis,
            ai_analysis=ai_detection,
            additional_metadata=additional_metadata,
        )

        self.url = "/api/inputrecords/"

    def test_save_and_retrieve_record(self):
        """
        Test the serialization, validation, and saving of an InputRecord instance.

        This method tests if an InputRecord can be serialized, validated, and saved correctly.
        It also checks the serialization output by saving it to a JSON file.
        This test ensures that the InputRecordSerializer can handle complex nested data.
        """
        # Serialize the data
        serializer = InputRecordSerializer(instance=self.input_record)
        serializer = InputRecordSerializer(data=serializer.data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        # print(json.dumps(serializer.data, indent=4))

        serializer.save()

        # Get today's date as a string
        today_str = datetime.now().strftime("%Y-%m-%d")

        # Define the file name and path
        filename = f"{today_str}.json"
        test_folder = os.path.join(settings.BASE_DIR, "..", "LogTests")
        file_path = os.path.join(test_folder, filename)

        # Ensure the test directory exists
        os.makedirs(test_folder, exist_ok=True)

        # Write the data to a JSON file
        with open(file_path, "w") as outfile:
            json.dump(serializer.data, outfile, indent=4)

    def test_api_create_input_record(self):
        """
        Test the creation of an InputRecord instance through the API.

        This method simulates a POST request to the API with the serialized data of an InputRecord instance.
        It then retrieves the list of all InputRecord instances via a GET request to ensure the new instance
        has been successfully created and is retrievable from the API.
        """
        serializer = InputRecordSerializer(instance=self.input_record)

        self.client.post(self.url, serializer.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
