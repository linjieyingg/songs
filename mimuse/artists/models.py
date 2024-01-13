from django.db import models
from songs.models import Song, Album

# Create your models here.

class Artist(models.Model):
    api_id = models.CharField(null=True, unique=True)
    name = models.CharField(max_length=100)
    overview = models.CharField(blank=True, default='')
    popularity = models.SmallIntegerField(null=True)
    followers = models.IntegerField(null=True)
    image = models.URLField(null=True)
    songs = models.ManyToManyField(Song)
    albums = models.ManyToManyField(Album)


    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.api_id