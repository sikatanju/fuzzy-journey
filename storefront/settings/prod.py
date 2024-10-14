import os

import dj_database_url

from .common import *


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['fuzzybuy-prod-5e420af0f5ab.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}

REDISCLOUD_URL = os.environ['REDISCLOUD_URL']

CELERY_BROKER_URL = REDISCLOUD_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDISCLOUD_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


smtp_info = dj_database_url.parse(os.getenv('CLOUDMAILIN_SMTP_URL'))

EMAIL_HOST = smtp_info['HOST']
EMAIL_PORT = smtp_info['PORT']
EMAIL_HOST_USER = smtp_info['USER']
EMAIL_HOST_PASSWORD = smtp_info['PASSWORD']