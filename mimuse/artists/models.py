from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    overview = models.CharField()
    popularity = models.SmallIntegerField()
    followers = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
    		return self.name