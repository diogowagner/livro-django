from .settings import *

DEBUG = True

SECRET_KEY = '@Kkjro2kIp=>kbvRPiV490874@n!jfw232!43*fnhIoQTC@9'

ALLOWED_HOSTS = ['159.112.186.174', 'localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}