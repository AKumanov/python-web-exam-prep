from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letter_validator(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def positive_num_validator(value):
    if value < 0:
        raise ValidationError('Budget should not be below zero.')


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size} MB'
