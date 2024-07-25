""" Settings file to run the project locally on the local OS using a virtual environment."""

from .development import *

DEBUG = False
ALLOWED_HOSTS = [
    "openmindszone.pythonanywhere.com",
    "www.openmindszone.pythonanywhere.com",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
