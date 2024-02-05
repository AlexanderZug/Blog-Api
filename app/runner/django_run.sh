#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py shell <<EOF
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

try:
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
except Exception:
    pass
EOF
python3 manage.py test
python3 manage.py runserver 0.0.0.0:8000
