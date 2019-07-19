from .base import *    # NOQA

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'u09021232',
        'HOST': '10.0.2.199',
        'PORT': '3306',
        #'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            #'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}