from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from my_music_app2.albums.models import Album


# Create your views here.


class AlbumDetails(DetailView):
    model = Album
    template_name = "album/album-details.html"



class AddAlbum(CreateView):
    model = Album
    fields = ["album_name", "artist", "genre", "description", "image_url", "price"]

    template_name = "album/album-add.html"

    labels = {
        "album_name": "Album Name",
        "artist": "Artist",
        "genre": "Genre",
        "description": "Description",
        "image_url": "Image URL",
        "price": "Price",
    }
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super().get_form(form_class)
        form.fields['album_name'].widget.attrs ={'placeholder': 'Album Name'}
        form.fields['artist'].widget.attrs ={'placeholder': 'Artist Name'}
        form.fields['description'].widget.attrs ={'placeholder': 'Description'}
        form.fields['image_url'].widget.attrs ={'placeholder': 'Image Url'}
        form.fields['price'].widget.attrs ={'placeholder': 'Price'}

        for field_name, label in self.labels.items():
            form.fields[field_name].label = label
        return form



