from django.db import models
from django.core import validators


class Category(models.Model):
    NAME_MAX_LENGTH = 15
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )


class Product(models.Model):
    NAME_MAX_LENGTH = 25
    PRICE_MIN_VALUE = 0.01
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(PRICE_MIN_VALUE),
        )
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
