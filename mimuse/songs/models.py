from django.db import models

# Create your models here.

class Album(models.Model):
    api_id = models.CharField(null=True, unique=True)
    title = models.CharField(null=True)
    release_date = models.DateField(null=True)
    cover_image = models.URLField(null=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
    	return self.api_id
    
class Song(models.Model):
    api_id = models.CharField(null=True, unique=True)
    title = models.CharField()
    album_id = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    release_date = models.DateField()
    popularity = models.SmallIntegerField()
    favorite = models.BooleanField(default=False)
    preview_url = models.URLField(null=True)
    
    class Meta:
        ordering = ['title']


    