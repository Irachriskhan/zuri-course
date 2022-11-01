from django.contrib import admin
from .models import Song
from .models import Lyric
from .models import Artiste

# Register your models here.
admin.site.register(Song)
admin.site.register(Artiste)
admin.site.register(Lyric)