DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cars',
        'USER': 'superuser',
        'PASSWORD': 'superuser',
        'HOST': 'db',
        'PORT': '5432',
    },
}
