
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='api_id',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
