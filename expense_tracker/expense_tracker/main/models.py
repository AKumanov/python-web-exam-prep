from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from .validators import only_letter_validator, positive_num_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            only_letter_validator,
        ]

    )
    last_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator,
            only_letter_validator
        ],
    )
    budget = models.FloatField(
        default=0,
        validators=[positive_num_validator]

    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        default='images/user.png',
        validators=[
            MaxFileSizeInMbValidator,
        ]
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Expense(models.Model):
    title = models.CharField(
        max_length=30
    )
    expense_image = models.URLField(

    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField(
        validators=[positive_num_validator, MinValueValidator(0)]
    )
