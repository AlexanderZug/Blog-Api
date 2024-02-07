import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

app = Celery("django_app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "make_verify_token_cleanup": {
        "task": "account.tasks.verify_token_cleanup_scheduler",
        "schedule": 120.0,
    }
}

app.conf.beat_schedule = {
    "send_email_notification": {
        "task": "account.tasks.send_email_notification",
        "schedule": crontab(hour=10, minute=0),
    }
}
