"""
Django settings for DjangoSite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9&ga^g*m^v3_x)%oguls$86fao-tofqn#vx0(wkrjy&m+b^^nf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoAPP',
    'django.contrib.admin',
    'south',
    'sorl.thumbnail',
    'topnotchdev.files_widget'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoSite.urls'

WSGI_APPLICATION = 'DjangoSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-site',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_FINDERS =\
    global_settings.STATICFILES_FINDERS +\
    ('django.contrib.staticfiles.finders.AppDirectoriesFinder',
     'django.contrib.staticfiles.finders.FileSystemFinder', )

TEMPLATE_CONTEXT_PROCESSORS =\
    global_settings.TEMPLATE_CONTEXT_PROCESSORS +\
    ("django.core.context_processors.request", )

GOOGLE_MAPS_API_KEY = 'AIzaSyBEx6VSQzHSqbNHykcI1TDSA0Om3h8ujaU'
GOOGLE_MAPS_URL = 'https://maps.googleapis.com/maps/api/js?v=3.exp&key=%s&sensor=false'

DEFAULT_MAP_CENTRE = -33.896281, 151.179963
DEFAULT_MAP_ZOOM = 15

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'