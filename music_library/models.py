from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Music_Library(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(datetime)
    genre = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='liked_songs')
    dislikes = models.ManyToManyField(User, related_name='disliked_songs')
