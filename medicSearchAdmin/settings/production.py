from .settings import *

DEBUG = False

SECRET_KEY = '@w232!43*fnhIoQTCkIp=>kbvRPiKkjro20874@n!jfV49@9'

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Nome do banco de dados',
        'USER': 'Nome do usuário',
        'PASSWORD': 'Senha',
        'HOST': 'Nome do host de conexão ao banco',
        'PORT': 'Número da porta de comunicação',
    }
}