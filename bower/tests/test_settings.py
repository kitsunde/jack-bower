import os

DEBUG = True

SITE_ID = 1

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')

STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    'bower',
    'bower.tests.test_app',
]

SECRET_KEY = 'foobar'

TEST_RUNNER = 'discover_runner.DiscoverRunner'
