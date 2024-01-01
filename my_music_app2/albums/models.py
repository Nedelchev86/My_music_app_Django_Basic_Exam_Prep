from django.core import validators
from django.db import models

from my_music_app2.users.models import Profile

# Create your models here.

GENRES = (
    ("pop", "Pop Music"),
    ("jazz", "Jazz Music"),
    ("rnb", "R&B Music"),
    ("rock", "Rock Music"),
    ("country", "Country Music"),
    ("dance", "Dance Music"),
    ("hiphop", "Hip Hop Music"),
    ("other", "Other"),
    )


class Album(models.Model):
    album_name = models.CharField(
        null=False,
        blank=True,
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
        null=False,
        blank=True,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=GENRES
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(0.0)]
    )

    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)


