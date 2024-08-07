"""
Django settings for products_prices project.

Generated by 'django-admin startproject' using Django 5.0.6.
"""

import os
from pathlib import Path

import sentry_sdk

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# We generate a new fresh SECRET_KEY to every new project,
# and keep it in a local uncommited file.
# Make sire that .secret_key is added to .gitignore.

try:
    from .secret_key import SECRET_KEY
except ImportError:
    # Exceptionally not importing on top, once is one-time use.
    from django.core.management.utils import get_random_secret_key

    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(SETTINGS_DIR + "/secret_key.py"), "w") as file:
        file.write("SECRET_KEY = '" + get_random_secret_key() + "'\n")

    from .secret_key import SECRET_KEY  # noqa: F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "openmindszone.pythonanywhere.com",
    "www.openmindszone.pythonanywhere.com",
]


# Application definition

INSTALLED_APPS = [
    # Core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    # Local apps
    "products.apps.ProductsConfig",
    "accounts.apps.AccountsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "products_prices.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "products_prices.context_processors.date_context_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "products_prices.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "products:home"
LOGOUT_REDIRECT_URL = "products:home"

INTERNAL_IPS = (
    "127.0.0.1",
    "0.0.0.0",
    "localhost",
)

sentry_sdk.init(
    dsn="https://cc136189afcedb53a543c7f7cc77f60c@o4507621255348224.ingest.de.sentry.io/4507639375986768",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
