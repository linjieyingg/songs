# Generated by Django 5.0.1 on 2024-01-15 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0012_song_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(blank=True),
        ),
    ]
