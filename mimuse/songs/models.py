from django.db import models
# Create your models here.

class Album(models.Model):
    api_id = models.CharField(null=True, unique=True)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_image = models.URLField(null=True)
    
    class Meta:
        ordering = ['title']
    
class Song(models.Model):
    api_id = models.CharField(null=True, unique=True)
    title = models.CharField(max_length=100)
    album_id = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    release_date = models.DateField()
    popularity = models.SmallIntegerField()
    favorite = models.BooleanField(default=False)
    preview_url = models.URLField(null=True)
    
    class Meta:
        ordering = ['title']


    