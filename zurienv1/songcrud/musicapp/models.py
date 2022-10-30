from django.db import models
from django.db.models import Model

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_released = models.DateField()
    likes = models.IntegerField()
    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song,on_delete = models.CASCADE)
    content = models.CharField(max_length= 1000)

# there is a relationship between all three Models.
#  An Artiste can have multiple songs, 
# song can have multiple lyrics.
# A song must only belong to one Artiste and a lyric must only belong to a song