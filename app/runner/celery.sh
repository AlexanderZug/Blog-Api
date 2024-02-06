#!/bin/bash

python3 manage.py migrate
celery -A django_app worker -B -E -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
