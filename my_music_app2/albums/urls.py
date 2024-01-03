from django.urls import path

from my_music_app2.albums.views import AlbumDetails

urlpatterns = [
    path('<int:pk>/details/', AlbumDetails.as_view(), name='album_details'),
]
