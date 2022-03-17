from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from testing_demos.common.validators import validate_only_letters


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=25,
        validators=(
            validate_only_letters,
        ),
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(150),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
