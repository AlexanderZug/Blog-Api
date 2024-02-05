import os
from dotenv import load_dotenv

from .settings import *

load_dotenv(BASE_DIR.parent.parent / ".env")

INSTALLED_APPS += ["drf_yasg", "rest_framework", "drf_spectacular"]

FRONTEND_MODULES = ["api"]

INSTALLED_APPS += FRONTEND_MODULES

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "api/media/"

STATIC_URL = "api/static/"
STATIC_ROOT = BASE_DIR / "static"

LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/Berlin"

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "secret_key")

DEBUG = os.environ.get("DEBUG", True)
ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTS", "*")]
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DJANGO_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DJANGO_DB_HOST", "localhost"),
        "PORT": os.environ.get("DJANGO_DB_PORT", "5432"),
    }
}
PROJECT_NAME = "Template"
PROJECT_DESCRIPTION = "Django Template"
API_INFO = {
    "title": f"{PROJECT_NAME} API",
    "description": f"API for {PROJECT_DESCRIPTION}",
    "version": "1.0.0",
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "django_app.auth.CsrfExemptSessionAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}
