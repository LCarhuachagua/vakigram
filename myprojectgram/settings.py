"""
Django settings for myprojectgram project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j+mld@wlz2&w1)@8*oxkpv4u^e0i)dys@)_!fhujxtpoe3qwt6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'app1',
    'posts',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Relacionado con la seguridad
    'django.contrib.sessions.middleware.SessionMiddleware', # Relacionado con las sesiones
    'django.middleware.common.CommonMiddleware', # Relacionado con el funcionamiento de Django: debug, etc
    'django.middleware.csrf.CsrfViewMiddleware', # Relacionado con la validation de formularios
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Relacionado con la autenticación de usuarios (login) y permisos (grupos).
    'django.contrib.messages.middleware.MessageMiddleware', # Relacionado con el sistema de mensajes de Django (flash messages)
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Relacionado con el clickjacking (ataques a través de iframes)
    
    'myprojectgram.middleware.ProfileCompletionMiddleware', # Middleware de la app users
]

ROOT_URLCONF = 'myprojectgram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR /'templates',
        ],
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

WSGI_APPLICATION = 'myprojectgram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
#STATICFILES_FINDERS = [
 #   'django.contrib.staticfiles.finders.FileSystemFinder',
 #  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#]

MEDIA_ROOT = BASE_DIR /'media'
MEDIA_URL = 'media/'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = LOGIN_URL

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
