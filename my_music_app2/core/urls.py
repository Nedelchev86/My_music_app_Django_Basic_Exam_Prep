from django.urls import path

from my_music_app2.core.views import IndexView, CreateProfileView

urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path('create-profile/', CreateProfileView.as_view(), name='create_profile'),

]