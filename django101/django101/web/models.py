from django.db import models


class Category(models.Model):
    NAME_MAX_LEN = 15
    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    TITLE_MAX_LEN = 24

    # objects = ...

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
