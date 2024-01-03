from django.shortcuts import render
from django.views.generic import DetailView

from my_music_app2.albums.models import Album


# Create your views here.


class AlbumDetails(DetailView):
    model = Album
    template_name = "album/album-details.html"
