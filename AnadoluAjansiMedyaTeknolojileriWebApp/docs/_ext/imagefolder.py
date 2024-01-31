import os
import shutil
import django
from pathlib import Path
from sphinx.application import Sphinx

# Initialize Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_django_project.settings')
django.setup()

# Import your Django models
from image_generator.models import GeneratedImages

def generate_image_rst(app: Sphinx):
    source_image_folder = Path('C:/Users/muham/OneDrive/Masaüstü/Anadolu-Ajans--Medya-Teknolojileri-hackathon/AnadoluAjansiMedyaTeknolojileriWebApp/media/generated_images')
    static_image_folder = Path(app.srcdir) / '_static' / 'generated_images'
    output_file = Path(app.srcdir) / 'generated_images.rst'

    # Ensure static image directory exists
    static_image_folder.mkdir(parents=True, exist_ok=True)

    # Header for the RST file
    rst_content = "Generated Images\n================\n\n"

    # Query the Django model
    for image_model in GeneratedImages.objects.all().order_by('?'):
        file_name = os.path.basename(image_model.image.file.name)
        source_file = source_image_folder / file_name
        destination_file = static_image_folder / file_name

        # Check if file exists in the source directory
        if source_file.exists():
            # Copy image to _static directory
            shutil.copy(source_file, destination_file)

            # Add image and additional info to RST content
            rst_image_path = f"_static/generated_images/{file_name}"
            image_info = image_model.image_generation.news_context.headline
            
            # Using figure directive for images
            rst_content += f".. figure:: {rst_image_path}\n   :alt: {file_name}\n\n   {image_info}\n\n"
            
            rst_content += "\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rst_content)

def setup(app: Sphinx):
    app.connect("builder-inited", generate_image_rst)
