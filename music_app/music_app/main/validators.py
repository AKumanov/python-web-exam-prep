import re

from django.core.exceptions import ValidationError


def check_string_validator(value):
    outcome = re.match("^[A-Za-z0-9_]*$", value)
    if not outcome:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def check_positive_integer(value):
    if value < 0:
        raise ValidationError('Age cannot be below 0')


def check_price_validator(value):
    if value < 0:
        raise ValidationError('Price cannot be less than 0')
