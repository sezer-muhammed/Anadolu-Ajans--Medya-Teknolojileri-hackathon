# Generated by Django 5.0 on 2024-01-24 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visualelements',
            old_name='objects',
            new_name='object_details',
        ),
    ]
