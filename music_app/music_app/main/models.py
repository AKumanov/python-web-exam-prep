from django.core.validators import MinLengthValidator
from django.db import models
from .validators import check_string_validator, check_positive_integer, check_price_validator


class Profile(models.Model):
    MAX_CHARACTERS = 15
    MIN_CHARACTERS = 2

    username = models.CharField(
        max_length=MAX_CHARACTERS,
        validators=(
            MinLengthValidator(MIN_CHARACTERS),
            check_string_validator
        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(check_positive_integer,)
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    GENRE_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other')
    )

    MAX_CHARACTERS = 30
    album_name = models.CharField(
        max_length=MAX_CHARACTERS,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_CHARACTERS
    )
    genre = models.CharField(
        max_length=MAX_CHARACTERS,
        choices=GENRE_CHOICES
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField()
    price = models.FloatField(
        validators=(check_price_validator, )
    )


    def __str__(self):
        return self.album_name
