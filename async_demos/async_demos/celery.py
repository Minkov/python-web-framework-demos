import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_demos.settings')

app = Celery('async_demos')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
