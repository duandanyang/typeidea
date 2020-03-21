from .base import *    # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'Admin123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        #'CONN_MAX_AGE': 5 * 60,
        #'OPTIONS': {'charset': 'utf8mb4'}
    }
}

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']