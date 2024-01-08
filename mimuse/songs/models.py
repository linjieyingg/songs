from django.db import models

# Create your models here.
from artists.models import Artist

class Album(models.Model):
    api_id = models.CharField(null=True)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    
    class Meta:
        ordering = ['title']
    
class Song(models.Model):
    api_id = models.CharField(null=True)
    title = models.CharField(max_length=50)
    album_id = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    artists = models.ManyToManyField(Artist)
    release_date = models.DateField()
    popularity = models.SmallIntegerField()
    favorite = models.BooleanField(default=False)
    preview_url = models.CharField(unique=True)
    
    class Meta:
        ordering = ['title']


    