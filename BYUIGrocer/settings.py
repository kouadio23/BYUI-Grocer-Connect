"""
Django settings for BYUIGrocer project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url




# Define the base directory of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Build paths inside the project like this: BASE_DIR / 'subdir'...
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production..
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-qbi^39v#_&u3$5ul-!4+!#exqa2#5t^66ilv_ofkh-f@qr31wz'
SECRET_KEY = os.path.join('DJANGO_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True ( Development environment )
DEBUG = os.environ.get('DEBUG', default=True)  == 'True'


ALLOWED_HOSTS = ['*']

# HTTPS settings
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', default='True') == 'True'
# SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', default='True') == 'True'
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', default='True') == 'True'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'byuiGrocerConnect.apps.ByuigrocerconnectConfig',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BYUIGrocer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'BYUIGrocer.wsgi.application'
ASGI_APPLICATION = 'BYUIGrocer.asgi.application'




# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'byuigrocer',
#         'USER': 'postgres',
#         'PASSWORD': '@password@',
#         'HOST': 'localhost',
#         'PORT': '5432',  # Default port yep
#     }
# }


# if os.environ.get('DATABASE_URL'):
#     DATABASES = {
#         'default': os.environ.get('DATABASE_URL')
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ.get('DB_NAME'),
#             'USER': os.environ.get('DB_USER', default='postgres'),
#             'PASSWORD': os.environ.get('DB_PASSWORD', default='@password@'),
#             'HOST': os.environ.get('DB_HOST', default='localhost'),
#             'PORT': os.environ.get('DB_PORT', default='5432')
#         }
#     }



if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER', default='postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD', default='@password@'),
            'HOST': os.environ.get('DB_HOST', default='localhost'),
            'PORT': os.environ.get('DB_PORT', default='5432')
        }
    }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATICFILES_DIRS = [
    # Additional static files directory within the project
    os.path.join(BASE_DIR, 'static'),
    
    
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
