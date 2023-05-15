from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {}

if "DATABASE_URL" in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))