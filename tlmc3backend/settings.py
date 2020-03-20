"""
Django settings for tlmc3backend project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g5-nvohs@5**#60+gx8w_sf18f=1e*26-q7zf&7yt4l*wnzu4u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tlmapi.apps.TlmapiConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'background_task'
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

ROOT_URLCONF = 'tlmc3backend.urls'

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

WSGI_APPLICATION = 'tlmc3backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE' : 'djongo',
#         'NAME' : 'Cluster0',
#         'HOST' : 'mongodb+srv://tpponmat:123456tp@cluster0-kkqya.mongodb.net/test',
#         'USER' : 'tpponmat',
#         'PASSWORD' : '123456tp',
#    }
# }


DATABASES = {
  'default': {
     'ENGINE': 'djongo',
     'NAME': 'heroku_7l964bnt',
     'HOST' : 'mongodb://heroku_7l964bnt:123456tp$@ds013926.mlab.com:13926/heroku_7l964bnt',     
     'USER' : 'heroku_7l964bnt',       
     'PASSWORD' : '123456tp$',
  }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'myapp-djongo-db',
#     }
# }

# DATABASES = {
#   'default': {  
#     'ENGINE':   'djongo',
#     'NAME':     'Cluster0',
#     'CLIENT': {
#       'host': 'cluster0-kkqya.mongodb.net',
#       'port': 27017,
#       'username': 'tpponmat',
#       'password': '123456tp',
#       'authSource': 'test',
#     } 
#   },
# }


        # 'HOST' : 'mongodb+srv://cluster0-comvj.mongodb.net/test',

# mongodb+srv://cluster0-kkqya.mongodb.net/test

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
django_heroku.settings(locals())
