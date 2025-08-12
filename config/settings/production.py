from .base import *

DEBUG = False

# Add your production domain here
ALLOWED_HOSTS = ['your-production-domain.com']

# Use a more robust database for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Add any other production-specific settings here
