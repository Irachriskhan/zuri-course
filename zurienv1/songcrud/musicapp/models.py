from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
class Song(models.Model):
    artiste_id = models.IntegerField()
    title = models.CharField(max_length = 50)
    date_released = models.CharField(max_length=15)
    likes = models.IntegerField()
class Lyric(models.Model):
    song_id = models.IntegerField()
    content = models.CharField(max_length=25)

# there is a relationship between all three Models.
#  An Artiste can have multiple songs, 
# song can have multiple lyrics.
# A song must only belong to one Artiste and a lyric must only belong to a song