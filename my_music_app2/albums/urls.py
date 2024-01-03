from django.urls import path

from my_music_app2.albums.views import AlbumDetails, AddAlbum

urlpatterns = [
    path('<int:pk>/details/', AlbumDetails.as_view(), name='album_details'),
    path('album/add/', AddAlbum.as_view(), name='add_album'),
]
