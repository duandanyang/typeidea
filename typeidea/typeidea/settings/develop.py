from .base import *    # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    'debug_toolbar_line_profiler',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js'
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar_line_profiler.panel.ProfilingPanel',
]