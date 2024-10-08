# Generated by Django 5.0.1 on 2024-01-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_alter_artist_api_id_alter_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='followers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='overview',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='popularity',
            field=models.SmallIntegerField(null=True),
        ),
    ]
