from django.urls import path

from .views import create_fake_user

urlpatterns = (
    path('fake-register/', create_fake_user),
)

from .signals import *
