"""
https://docs.djangoproject.com/en/1.10/topics/settings/
https://docs.djangoproject.com/en/1.10/ref/settings/
https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
https://docs.djangoproject.com/en/1.10/topics/i18n/
https://docs.djangoproject.com/en/1.10/howto/static-files/
https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
"""
import os
from django.contrib import admin

admin.site.site_url = '/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'tournament/static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tournament/static/tournament'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tournament/media')

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
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'tournament/templates'),
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

TIME_ZONE = 'Europe/Kiev'

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

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'develtasks@gmail.com'
EMAIL_HOST_PASSWORD = 'devil666'

SECRET_KEY = 'u=+5=zvsd9snb+pbid1x9(qje#qa***8hr4ui#kwkf12ylvx^)'

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
"""
The "Recent Actions" panel in Django Admin displays LogEntry models.
To clear it you would just delete all the objects:

from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()
"""

"""
accounts:
coal coal123456
"""
