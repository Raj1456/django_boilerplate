from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip-address', 'www.yourwebsite.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your db name',
        'USER': 'your db username',
        'PASSWORD':'Your db password',
        'HOST':'localhost',
        'PORT':''
    }
}

STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_PRIVATE_KEY = 'your-live-secret-key'