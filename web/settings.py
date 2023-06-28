from environs import Env
env = Env()
env.read_env()

import os
from pathlib import Path
from .jazmin import JAZZMIN_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "post",
    "app",
    "ckeditor",
    "ckeditor_uploader",
    "django_social_share",
    "hitcount",
    # "web.contrib.admin",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "template"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "web.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


import dj_database_url

DATABASES = {
    "default": dj_database_url.parse(env.str('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "uz-uz"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ("uz", _("O`zbek tili")),
    ("en", _("Ingliz tili")),
)

LOCALE_PATHS = [BASE_DIR / "locale"]

MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"

MODELTRANSLATION_LANGUAGES = ("uz", "en")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Full",
    },
}

LOGIN_REDIRECT_URL = "post"
LOGOUT_REDIRECT_URL = "post"

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDTITOR_RESTRICT_BY_USER = True

# ==================================================================================================================

# JAZZMIN =======================

JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
# JAZZMIN_SETTINGS = {
#     'site_title': 'Mening Boshqaruv',
#     'site_header': 'Mening Boshqaruv',
#     'welcome_sign': 'Xush kelibsiz!',
#     'search_model': 'auth.User',
#     'user_menu': [
#         {'model': 'auth.user'},
#         {'app': 'myapp', 'label': 'Mening ilovam'},
#         ...
#     ],
# }
