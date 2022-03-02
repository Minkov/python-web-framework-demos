# Wrong
from django.contrib.auth.models import User

# Correct
from django.contrib.auth import get_user_model, authenticate
from django.db import models

UserModel = get_user_model()
UserModel.objects.create_user(
    username='doncho2',
    password='12345qwe',
)