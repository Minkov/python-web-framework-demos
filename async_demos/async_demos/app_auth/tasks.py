from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

UserModel = get_user_model()


@shared_task
def send_successful_registration_email(user_pk):
    user = UserModel.objects.get(pk=user_pk)
    context = {
        'name': 'Doncho',
    }
    message = render_to_string('successful_registration.html', context)
    send_mail(
        'Hello from us!',
        message,
        'doncho@minkov.it',
        (user.email,),
    )
