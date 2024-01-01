from django.core import validators

from django.db import models

from my_music_app2.users.validators import validate_string_contains_only_letters_numbers_and_underscore


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=[validators.MinLengthValidator(2), validate_string_contains_only_letters_numbers_and_underscore],
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(0)]
    )

