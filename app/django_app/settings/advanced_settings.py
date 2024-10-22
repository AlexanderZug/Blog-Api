import os

from dotenv import load_dotenv

from .settings import *

load_dotenv(BASE_DIR.parent.parent / ".env")

INSTALLED_APPS += [
    "drf_yasg",
    "rest_framework",
    "drf_spectacular",
    "django_celery_beat",
]

FRONTEND_MODULES = ["api.apps.ApiConfig", "blog.apps.BlogConfig", "account.apps.AccountConfig", "test_dump"]

INSTALLED_APPS += FRONTEND_MODULES

AUTH_USER_MODEL = "account.User"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "api/media/"

STATIC_URL = "api/static/"
STATIC_ROOT = BASE_DIR / "static"

LANGUAGE_CODE = "en"
TIME_ZONE = "Europe/Berlin"

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "secret_key")

DEBUG = os.environ.get("DEBUG", False)
ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTS", "*")]

# Celery Configuration Options
CELERY_RESULT_BACKEND = "redis://redis:6379" + "/0"
CELERY_BROKER_URL = "redis://redis:6379" + "/0"
CELERY_CACHE_BACKEND = "default"

LOCAL_DATABASE = os.environ.get("LOCAL_DATABASE", False)

if LOCAL_DATABASE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": Path("db.sqlite3"),
            "USER": os.environ.get("DB_USER", "user"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DJANGO_DB_ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("DB_NAME", "postgres"),
            "USER": os.environ.get("DB_USER", "postgres"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
            "HOST": os.environ.get("DB_HOST", "db"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }

PROJECT_NAME = "Blog"
PROJECT_DESCRIPTION = "Blog"
API_INFO = {
    "title": f"{PROJECT_NAME} API",
    "description": f"API for {PROJECT_DESCRIPTION}",
    "version": "1.0.0",
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "django_app.auth.CsrfExemptSessionAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

GRAPPELLI_INDEX_DASHBOARD = "django_app.dashboard.CustomIndexDashboard"
