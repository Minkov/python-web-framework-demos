from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.db import models

from auth_demos.auth_app.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


'''
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model:
```
AUTH_USER_MODEL = 'auth_app.AppUser' in settings.py
```
3. Create user manager manager
'''
