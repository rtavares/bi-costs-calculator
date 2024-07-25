""" Settings file to run the project locally on the local OS using a virtual environment."""

from .development import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASE_LOCATION =  BASE_DIR.resolve().parent / "db.sqlite3"
print(f"SqLite Database location: {DATABASE_LOCATION}")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASE_LOCATION,
    }
}
