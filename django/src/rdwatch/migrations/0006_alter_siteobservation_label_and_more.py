# Generated by Django 4.1.9 on 2023-05-04 11:42

import django.contrib.postgres.indexes
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rdwatch', '0005_alter_siteobservation_geom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteobservation',
            name='label',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='rdwatch.observationlabel',
            ),
        ),
        migrations.AlterField(
            model_name='siteobservation',
            name='siteeval',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='rdwatch.siteevaluation'
            ),
        ),
        migrations.CreateModel(
            name='SiteImage',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'timestamp',
                    models.DateTimeField(help_text="The source image's timestamp"),
                ),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                (
                    'cloudcover',
                    models.FloatField(
                        help_text='Cloud Cover associated with Image', null=True
                    ),
                ),
                (
                    'source',
                    models.CharField(
                        blank=True, help_text='WV, S2, L8 imagery source', max_length=2
                    ),
                ),
                (
                    'siteeval',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='rdwatch.siteevaluation',
                    ),
                ),
                (
                    'siteobs',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='rdwatch.siteobservation',
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name='siteimage',
            index=django.contrib.postgres.indexes.GistIndex(
                fields=['timestamp'], name='rdwatch_sit_timesta_808546_gist'
            ),
        ),
    ]
