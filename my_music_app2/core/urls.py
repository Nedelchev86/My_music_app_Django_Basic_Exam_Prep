from django.urls import path

from my_music_app2.core.views import IndexView, HomePageNoProfile

urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path('create-profile/', HomePageNoProfile.as_view(), name='create_profile'),

]