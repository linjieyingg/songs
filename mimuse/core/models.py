from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    api_key = models.CharField()
    api_key2 = models.CharField(blank=True)