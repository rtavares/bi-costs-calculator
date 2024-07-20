""" Settings file to deploy project to a production environment, containerized."""
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']  # To be changed

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}