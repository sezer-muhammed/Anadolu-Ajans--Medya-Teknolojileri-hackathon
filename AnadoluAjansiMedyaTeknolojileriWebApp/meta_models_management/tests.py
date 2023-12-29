from django.test import TestCase
from .models import *
from .serializers import InputRecordSerializer
from faker import Faker
import random

class InputRecordSerializerTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()

        # Create related objects
        # Location
        location = SourceLocation.objects.create(
            latitude=float(self.faker.latitude()), 
            longitude=float(self.faker.longitude())
        )

        # SourceInfo
        source_info = SourceInfo.objects.create(
            source=self.faker.company(), 
            city=self.faker.city(), 
            country=self.faker.country(), 
            location=location
        )

        # ContentAnalysis
        content_analysis = ContentAnalysis.objects.create(
            detailed_description=self.faker.text(), 
            summary=self.faker.sentence()
        )
        for _ in range(5):
            keyword = Keyword.objects.create(value=self.faker.word())
            content_analysis.keywords.add(keyword)

        # EmotionAnalysis
        emotion_analysis = EmotionAnalysis.objects.create()
        for _ in range(3):
            emotion = AssociatedEmotion.objects.create(emotion=self.faker.word())
            emotion_analysis.associated_emotions.add(emotion)

        # AIDetection
        ai_detection = AIDetection.objects.create(emotion_analysis=emotion_analysis)
        for _ in range(3):
            obj = Object.objects.create(
                name=self.faker.word(), 
                status=self.faker.word(), 
                action=self.faker.word()
            )
            ai_detection.object_detection.add(obj)
        for _ in range(3):
            text = TextExtraction.objects.create(text=self.faker.sentence())
            ai_detection.text_extraction.add(text)

        # AdditionalMetadata
        additional_metadata = AdditionalMetadata.objects.create()

        for _ in range(3):
            attribute = SourceAttribute.objects.create(attribute=self.faker.word())
            additional_metadata.source_attributes.add(attribute)
        
        for _ in range(3):
            theme = ContentTheme.objects.create(theme=self.faker.word())
            additional_metadata.content_themes.add(theme)
        
        for _ in range(3):
            audience_type = Audience.objects.create(audience_type=self.faker.word())
            additional_metadata.audience.add(audience_type)
        
        for _ in range(3):
            geography = GeographicRelevance.objects.create(geography=self.faker.word())
            additional_metadata.geographic_relevance.add(geography)
        
        for _ in range(3):
            temporal = TemporalRelevance.objects.create(temporal=self.faker.date())
            additional_metadata.temporal_relevance.add(temporal)
        
        for _ in range(3):
            level = TechnicalLevel.objects.create(level=self.faker.word())
            additional_metadata.technical_level.add(level)
        
        for _ in range(3):
            trend = SentimentTrend.objects.create(trend=self.faker.word())
            additional_metadata.sentiment_trends.add(trend)
        
        for _ in range(3):
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
            additional_metadata=additional_metadata
        )

    def test_save_and_retrieve_record(self):
        # Serialize the data
        serializer = InputRecordSerializer(instance=self.input_record)
        serializer = InputRecordSerializer(data=serializer.data)

        self.assertTrue(serializer.is_valid(), serializer.errors)

