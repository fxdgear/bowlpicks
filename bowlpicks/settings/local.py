from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bowlpicks',                      # Or path to database file if using sqlite3.
        'USER': 'nicklang',                      # Not used with sqlite3.
        'PASSWORD': 'd3n4lirulz',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += ['debug_toolbar']
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# send emails to the console
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
