# Generated by Django 5.0.1 on 2024-01-10 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_album_cover_image_alter_song_preview_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artists',
        ),
    ]
