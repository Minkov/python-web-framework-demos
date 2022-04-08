from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from async_demos.app_auth.tasks import send_successful_registration_email

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(instance, created, *args, **kwargs):
    if not created:
        return

    send_successful_registration_email.delay(instance.pk)
