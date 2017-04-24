import os
from django.contrib import admin
# from light_it_task.sets.base import *
admin.site.site_url = '/'

SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SETTINGS_DIR)
PROJECT_ROOT = os.path.dirname(BASE_DIR)
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'tournament/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'tournament/media')

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'skyrocker.pythonanywhere.com', 'tourns.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tournament',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.facebook',
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

ROOT_URLCONF = 'light_it_task.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_PATH,
            os.path.join(PROJECT_ROOT, 'tournament/templates'),
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

WSGI_APPLICATION = 'light_it_task.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_SIGNUP_FORM_CLASS = 'tournament.forms.NewPlayer'

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': ['id', 'email', 'first_name', 'last_name', 'gender']
        },
    'vk': {
        'SCOPE': ['email', 'public_profile'],
        'FIELDS': ['id', 'email', 'first_name', 'last_name', 'gender'],
        },
    }

VK_ID = 5742876
VK_KEY = 'RVOQtGVScBSHMWqyo1l9'

FB_ID = 1310090682374732
FB_KEY = '25947fd470d66a39bf6267a5abb50700'

SECRET_KEY = os.environ['DJANGO_TOURN_KEY']

"""
from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()
"""
