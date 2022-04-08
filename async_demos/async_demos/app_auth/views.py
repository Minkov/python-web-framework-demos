import random

from django.contrib.auth import get_user_model
from django.http import HttpResponse

from django.contrib.auth.views import PasswordResetView
UserModel = get_user_model()


def create_fake_user(request):
    rand_count = 6

    username_suffix = ''.join(str(random.randint(1, 1000)) for _ in range(rand_count))
    UserModel.objects.create_user(
        username=f'doncho_{username_suffix}',
        password='1sxaSD@##!2$%12@#SXHHJS))0001912039123980-12-',
        email='mejarak400@procowork.com',
    )
    return HttpResponse('It works')
