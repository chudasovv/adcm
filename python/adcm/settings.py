# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Django settings for adcm project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import json
import os
from os.path import dirname

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))
CONF_DIR = BASE_DIR + '/data/conf/'
SECRET_KEY_FILE = CONF_DIR + '/secret_key.txt'
CONFIG_FILE = BASE_DIR + '/config.json'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Load secret key from filesystem
if os.path.exists(SECRET_KEY_FILE):
    with open(SECRET_KEY_FILE, encoding='utf_8') as f:
        SECRET_KEY = f.read().strip()
else:
    # If we have no SECRET_KEY_FILE than we are running in some tricky fashion.
    # In that case we will use random key every run. That is usefull for
    # manage.py calls during image build
    SECRET_KEY = get_random_secret_key()

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, encoding='utf_8') as f:
        ADCM_VERSION = json.load(f)['version']
else:
    ADCM_VERSION = '2019.02.07.00'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django_generate_secret_key',
    'django_filters',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'background_task',
    'rest_framework',
    'rest_framework_swagger',
    'api.apps.APIConfig',
    'corsheaders',
    'rest_framework.authtoken',
    'social_django',
    'guardian',
    'rbac',
    'adwp_events',
    'cm.apps.CmConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'adcm.urls'

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

WSGI_APPLICATION = 'adcm.wsgi.application'
LOGIN_URL = '/admin/login/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.DjangoModelPermissions'
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ],
    'EXCEPTION_HANDLER': 'cm.errors.custom_drf_exception_handler',
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/var/cluster.db'),
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'adcm',
        # 'HOST': 'localhost',
        # 'USER': 'adcm',
        # 'PASSWORD': 'adcm',
        'OPTIONS': {
            'timeout': 20,
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    'social_core.backends.google.GoogleOAuth2',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'cm.views.get_token',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = []
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'wwwroot/static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static"
    # Don't forget to use absolute paths, not relative paths.
)

ADWP_EVENT_SERVER = {
    # path to json file with Event Server secret token
    'SECRETS_FILE': os.path.join(BASE_DIR, 'data/var/secrets.json'),
    # URL of Event Server REST API
    'API_URL': 'http://localhost:8020/api/v1',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'adwp': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'formatter': 'adwp',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'data/log/adcm_debug.log'),
        },
        'adwp_file': {
            'level': 'DEBUG',
            'formatter': 'adwp',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'data/log/adwp.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.utils.autoreload': {
            'level': 'INFO',
        },
        'adwp': {
            'handlers': ['adwp_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
