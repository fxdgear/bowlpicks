DEBUG = True

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


# send emails to the console
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'