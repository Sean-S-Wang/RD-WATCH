# Generated by Django 4.1.9 on 2023-07-24 12:41

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rdwatch', '0010_hyperparameters_evaluation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteimage',
            name='aws_location',
            field=models.CharField(
                blank=True,
                help_text='S3 Link to base file used to download this image',
                max_length=2048,
            ),
        ),
        migrations.AddField(
            model_name='siteimage',
            name='image_bbox',
            field=django.contrib.gis.db.models.fields.PolygonField(
                blank=True, help_text='Image Bounding Box', null=True, srid=4326
            ),
        ),
        migrations.AddField(
            model_name='siteimage',
            name='image_dimensions',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(), null=True, size=2
            ),
        ),
    ]
