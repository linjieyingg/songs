# Generated by Django 5.0.1 on 2024-01-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_alter_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
