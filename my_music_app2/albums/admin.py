from django.contrib import admin

from my_music_app2.albums.models import Album


# Register your models here.
@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    pass
