import os
from celery import Celery

# associate a Celery environment variable called DJANGO_SETTINGS_MODULE with the Django project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bboard.settings')

app = Celery('bboard')

# get celery configurations from projects' settings
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
