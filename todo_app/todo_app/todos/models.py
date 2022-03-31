from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    NAME_MAX_LENGTH = 15
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )


class Todo(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField()

    is_done = models.BooleanField(
        default=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.pk}: {self.title}'
