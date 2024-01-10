import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    """
    Validate the file extension of the given file.

    Parameters:
    value (File): The file to be validated.

    Raises:
    ValidationError: If the file extension is not supported.

    Returns:
    None
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".mp3", ".wav", ".ogg", ".m4a"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")
