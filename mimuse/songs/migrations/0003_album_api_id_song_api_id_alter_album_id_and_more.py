
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_album_id_alter_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='api_id',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='api_id',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
