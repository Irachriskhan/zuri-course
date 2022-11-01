from django.db import models
from django.db.models import Model
# from django.utils import timezone

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_released = models.DateField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song,on_delete = models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.song_id

# there is a relationship between all three Models.
#  An Artiste can have multiple songs, 
# song can have multiple lyrics.
# A song must only belong to one Artiste and a lyric must only belong to a song