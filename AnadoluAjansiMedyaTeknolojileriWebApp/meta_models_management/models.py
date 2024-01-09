from django.db import models


# Models for each list of strings
class Keyword(models.Model):
    """
    Represents a keyword associated with some content.

    Attributes
    ----------
    value : models.CharField
        The keyword text itself.
    """

    value = models.CharField(max_length=200)

    def __str__(self):
        """Returns the string representation of the Keyword."""
        return self.value


class AssociatedEmotion(models.Model):
    """
    Represents an emotion associated with some content.

    Attributes
    ----------
    emotion : models.CharField
        The type or name of the emotion.
    """

    emotion = models.CharField(max_length=200)

    def __str__(self):
        """Returns the string representation of the AssociatedEmotion."""
        return self.emotion


class Object(models.Model):
    """
    Represents an object detected in an image or video.

    Attributes
    ----------
    name : models.CharField
        The name of the object.
    status : models.CharField
        The status or condition of the object.
    action : models.CharField
        The action or activity associated with the object.
    """

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    action = models.CharField(max_length=200)

    def __str__(self):
        """Returns a formatted string representation of the Object."""
        return f"{self.name} ({self.status}) - {self.action}"


class TextExtraction(models.Model):
    """
    Represents an extracted piece of text, typically from a larger document or data source.

    Attributes
    ----------
    text : models.CharField
        The extracted text content, limited to a certain length.
    """

    text = models.CharField(max_length=1000)

    def __str__(self):
        """
        Provides a shortened string representation of the TextExtraction object.

        Returns
        -------
        str
            The first 50 characters of the extracted text followed by an ellipsis if the text is longer than 50 characters.
            Returns the entire text if it's shorter than 50 characters.
        """
        # Returns the first 50 characters plus an ellipsis if the text is longer
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text


class SourceAttribute(models.Model):
    """
    Represents an attribute or characteristic of a source, typically used to describe additional metadata.

    Attributes
    ----------
    attribute : models.CharField
        The descriptive text of the source's attribute.
    """

    attribute = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the SourceAttribute object.

        Returns
        -------
        str
            The text of the attribute itself.
        """
        return self.attribute


class ContentTheme(models.Model):
    """
    Represents the theme of a piece of content, typically used to categorize or describe the main subject matter.

    Attributes
    ----------
    theme : models.CharField
        The descriptive name or category of the content's theme.
    """

    theme = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the ContentTheme object.

        Returns
        -------
        str
            The text of the theme itself.
        """
        return self.theme


class Audience(models.Model):
    """
    Represents a type or category of audience for which the content is intended or most relevant.

    Attributes
    ----------
    audience_type : models.CharField
        The descriptive name or category of the audience type.
    """

    audience_type = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the Audience object.

        Returns
        -------
        str
            The text of the audience type itself.
        """
        return self.audience_type


class GeographicRelevance(models.Model):
    """
    Represents the geographic relevance or focus of a piece of content, typically used to indicate the area or region the content is pertinent to.

    Attributes
    ----------
    geography : models.CharField
        The descriptive name or identifier of the geographic area or region.
    """

    geography = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the GeographicRelevance object.

        Returns
        -------
        str
            The text of the geographic relevance or area itself.
        """
        return self.geography


class TemporalRelevance(models.Model):
    """
    Represents the time-related relevance or significance of a piece of content, typically used to indicate the period or era the content is pertinent to.

    Attributes
    ----------
    temporal : models.CharField
        The descriptive name or identifier of the temporal relevance, such as a date, period, or era.
    """

    temporal = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the TemporalRelevance object.

        Returns
        -------
        str
            The text of the temporal relevance or period itself.
        """
        return self.temporal


class TechnicalLevel(models.Model):
    """
    Represents the technical level or complexity of a piece of content, typically used to indicate the expertise required to understand or interact with the content.

    Attributes
    ----------
    level : models.CharField
        The descriptive name or identifier of the technical level, such as 'Beginner', 'Intermediate', or 'Expert'.
    """

    level = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the TechnicalLevel object.

        Returns
        -------
        str
            The text of the technical level itself.
        """
        return self.level


class SentimentTrend(models.Model):
    """
    Represents the sentiment trend associated with a piece of content, typically used to categorize the general feeling or attitude conveyed by the content.

    Attributes
    ----------
    trend : models.CharField
        The descriptive name or identifier of the sentiment trend, such as 'Positive', 'Negative', or 'Neutral'.
    """

    trend = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the SentimentTrend object.

        Returns
        -------
        str
            The text of the sentiment trend itself.
        """
        return self.trend


class InfluencerTag(models.Model):
    """
    Represents a tag associated with an influencer or prominent figure, typically used to categorize or describe the themes and topics they are known for.

    Parameters
    ----------
    tag : str
        The descriptive name or identifier of the influencer tag.

    Attributes
    ----------
    tag : models.CharField
        The descriptive name or identifier of the influencer tag.
    """

    tag = models.CharField(max_length=200)

    def __str__(self):
        """
        Provides the string representation of the InfluencerTag object.

        Returns
        -------
        str
            The text of the influencer tag itself.
        """
        return self.tag


# Main models
class SourceLocation(models.Model):
    """
    Represents a geographical location with latitude and longitude, typically used to indicate where an event occurred or where a piece of content is relevant.

    Attributes
    ----------
    latitude : models.FloatField
        The latitude of the location. Positive values indicate latitudes north of the equator, and negative values indicate latitudes south.
    longitude : models.FloatField
        The longitude of the location. Positive values indicate longitudes east of the Prime Meridian, and negative values indicate longitudes west.
    """

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        """
        Provides the string representation of the SourceLocation object.

        Returns
        -------
        str
            A formatted string displaying the latitude and longitude of the location.
        """
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"


class SourceInfo(models.Model):
    """
    Represents the source information, typically used to describe where or from whom a piece of content originates.

    Attributes
    ----------
    source : models.CharField
        The name or description of the source, such as a person, organization, or publication.
    city : models.CharField
        The city where the source is located or relevant to.
    country : models.CharField
        The country where the source is located or relevant to.
    location : models.OneToOneField
        A OneToOne relationship to the SourceLocation model, representing the geographical coordinates of the source.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    source = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    location = models.OneToOneField(SourceLocation, on_delete=models.CASCADE)

    def __str__(self):
        """
        Provides the string representation of the SourceInfo object.

        Returns
        -------
        str
            A formatted string displaying the source's name, city, and country.
        """
        return f"{self.source} - {self.city}, {self.country}"


class ContentAnalysis(models.Model):
    """
    Represents the analysis of content, including detailed descriptions, summaries, and associated keywords.

    Attributes
    ----------
    detailed_description : models.TextField
        A detailed description of the content being analyzed.
    summary : models.TextField
        A summarized version of the content for quick reference.
    keywords : models.ManyToManyField
        A ManyToMany relationship to the Keyword model, representing associated keywords related to the content analysis.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    detailed_description = models.TextField()
    summary = models.TextField()
    keywords = models.ManyToManyField(Keyword, related_name="content_analysis_keywords")

    def __str__(self):
        """
        Provides the string representation of the ContentAnalysis object.

        Returns
        -------
        str
            A truncated summary of the content analysis for display.
        """
        return self.summary[:50] + "..."


class EmotionAnalysis(models.Model):
    """
    Represents the analysis of emotions associated with content.

    Attributes
    ----------
    associated_emotions : models.ManyToManyField
        A ManyToMany relationship to the AssociatedEmotion model, representing associated emotions related to the analysis.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    associated_emotions = models.ManyToManyField(
        AssociatedEmotion, related_name="emotion_analysis_emotions"
    )

    def __str__(self):
        """
        Provides the string representation of the EmotionAnalysis object.

        Returns
        -------
        str
            A concatenated string of the first three associated emotions followed by an ellipsis.
        """
        return (
            ", ".join(
                [emotion.emotion for emotion in self.associated_emotions.all()[:3]]
            )
            + "..."
        )


class AIDetection(models.Model):
    """
    Represents the AI detection and analysis of content.

    Attributes
    ----------
    emotion_analysis : models.OneToOneField
        A one-to-one relationship to the EmotionAnalysis model, representing the associated emotion analysis.
    object_detection : models.ManyToManyField
        A ManyToMany relationship to the Object model, representing objects detected in the content.
    text_extraction : models.ManyToManyField
        A ManyToMany relationship to the TextExtraction model, representing extracted text from the content.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    emotion_analysis = models.OneToOneField(EmotionAnalysis, on_delete=models.CASCADE)
    object_detection = models.ManyToManyField(
        Object, related_name="ai_detection_objects"
    )
    text_extraction = models.ManyToManyField(
        TextExtraction, related_name="ai_detection_texts"
    )

    def __str__(self):
        """
        Provides the string representation of the AIDetection object.

        Returns
        -------
        str
            A string containing "AIDetection" followed by the object's ID.
        """
        return f"AIDetection {self.id}"


class AdditionalMetadata(models.Model):
    """
    Represents additional metadata associated with content.

    Attributes
    ----------
    source_attributes : models.ManyToManyField
        A ManyToMany relationship to the SourceAttribute model, representing source-specific attributes.
    content_themes : models.ManyToManyField
        A ManyToMany relationship to the ContentTheme model, representing content themes.
    audience : models.ManyToManyField
        A ManyToMany relationship to the Audience model, representing the target audience types.
    geographic_relevance : models.ManyToManyField
        A ManyToMany relationship to the GeographicRelevance model, representing geographic relevance.
    temporal_relevance : models.ManyToManyField
        A ManyToMany relationship to the TemporalRelevance model, representing temporal relevance.
    technical_level : models.ManyToManyField
        A ManyToMany relationship to the TechnicalLevel model, representing technical levels.
    sentiment_trends : models.ManyToManyField
        A ManyToMany relationship to the SentimentTrend model, representing sentiment trends.
    influencer_tags : models.ManyToManyField
        A ManyToMany relationship to the InfluencerTag model, representing influencer tags.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    source_attributes = models.ManyToManyField(
        SourceAttribute,
        related_name="additional_metadata_source_attributes",
        blank=True,
    )
    content_themes = models.ManyToManyField(
        ContentTheme, related_name="additional_metadata_content_themes", blank=True
    )
    audience = models.ManyToManyField(
        Audience, related_name="additional_metadata_audience", blank=True
    )
    geographic_relevance = models.ManyToManyField(
        GeographicRelevance,
        related_name="additional_metadata_geographic_relevance",
        blank=True,
    )
    temporal_relevance = models.ManyToManyField(
        TemporalRelevance,
        related_name="additional_metadata_temporal_relevance",
        blank=True,
    )
    technical_level = models.ManyToManyField(
        TechnicalLevel, related_name="additional_metadata_technical_level", blank=True
    )
    sentiment_trends = models.ManyToManyField(
        SentimentTrend, related_name="additional_metadata_sentiment_trends", blank=True
    )
    influencer_tags = models.ManyToManyField(
        InfluencerTag, related_name="additional_metadata_influencer_tags", blank=True
    )

    def __str__(self):
        """
        Provides the string representation of the AdditionalMetadata object.

        Returns
        -------
        str
            A string containing "Metadata" followed by the object's ID.
        """
        return f"Metadata {self.id}"


class InputRecord(models.Model):
    """
    Represents an input record with associated metadata and analyses.

    Attributes
    ----------
    input_id : str
        A unique identifier for the input record.
    input_type : str
        The type or category of the input.
    timestamp : str
        A string representing the timestamp of the input record.
        Consider using DateTimeField if the format is consistent.
    source_info : SourceInfo
        A one-to-one relationship to the SourceInfo model, representing the source information.
    content_analysis : ContentAnalysis
        A one-to-one relationship to the ContentAnalysis model, representing content analysis data.
    ai_analysis : AIDetection
        A one-to-one relationship to the AIDetection model, representing AI analysis data.
    additional_metadata : AdditionalMetadata
        A one-to-one relationship to the AdditionalMetadata model, representing additional metadata.

    Methods
    -------
    __str__(self)
        Returns a human-readable string representation of the object.
    """

    input_id = models.CharField(max_length=400)
    input_type = models.CharField(max_length=50)
    timestamp = models.CharField(
        max_length=50
    )  # Consider using DateTimeField if the format is consistent
    source_info = models.OneToOneField(SourceInfo, on_delete=models.CASCADE)
    content_analysis = models.OneToOneField(ContentAnalysis, on_delete=models.CASCADE)
    ai_analysis = models.OneToOneField(AIDetection, on_delete=models.CASCADE)
    additional_metadata = models.OneToOneField(
        AdditionalMetadata, on_delete=models.CASCADE
    )

    def __str__(self):
        """
        Provides the string representation of the InputRecord object.

        Returns
        -------
        str
            A string containing the input_id, input_type, and timestamp.
        """
        return f"{self.input_id} - {self.input_type} at {self.timestamp}"
