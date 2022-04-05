from django.core.exceptions import ValidationError
from django.db import models


def validate_letters_numbers_space(value):
    for ch in value:
        if not (ch.isdigit() or ch.isalpha() or ch == ' '):
            raise ValidationError


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Todo(models.Model):
    title = models.CharField(
        max_length=25,
        validators=(
            validate_letters_numbers_space,
        ),
    )

    def __str__(self):
        return f'{self.id}: {self.title}'
