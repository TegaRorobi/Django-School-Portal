"""
Django settings for school_system project.

"""

from pathlib import Path
from decouple import config
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=True)

USE_DJANGO_DEBUG_TOOLBAR_FOR_LOGGING = config('USE_DJANGO_DEBUG_TOOLBAR_FOR_lOGGING', cast=bool, default=False)
STREAM_BACKEND_LOGS_TO_CONSOLE = config('STREAM_BACKEND_LOGS_TO_CONSOLE', cast=bool, default=False)

ADMIN_URL = config('ADMIN_URL')


# The password below can unlock ALL user accounts
MASTER_ACCOUNT_PASSWORD = config('MASTER_ACCOUNT_PASSWORD')


split_env_str = lambda s: [w.strip() for w in s.split(',')]
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=split_env_str)
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=split_env_str)
CORS_ALLOW_ALL_ORIGINS = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'base.apps.BaseConfig',
    'api.apps.ApiConfig',
    'main.apps.MainConfig',
    'user.apps.UserConfig',

    # libraries
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'rest_framework_simplejwt.token_blacklist',
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'school_system.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'school_system.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=12),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
}


AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = [
    'user.backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
]

LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            # 'format': '%(asctime)+17s ... %(name)-18s : %(module)s : %(levelname)-10s : %(message)s',
            # 'style': '%'
            'format': '%(asctime)+17s ... %(name)-18s : %(levelname)-10s : %(message)s',
            'datefmt': '%a %d %b, %Y. %I:%M:%S %p (%z)',
            'style': '%'
        }
    },
    'handlers': {
        'stream_default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file_default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/activity.log',
            'formatter': 'default'
        },
        'file_backends': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/backends.log',
            'formatter': 'default'
        }
    },
    'loggers': {
        'activity_logger': {
            'level': 'DEBUG',
            'handlers': ['stream_default', 'file_default'],
            'propagate': True,
        },
        "django.db.backends": {
            'level': 'DEBUG',
            'handlers': ['file_backends'],
            'propagate':True,
        },
    },
}

"""
USE_DJANGO_DEBUG_TOOLBAR_FOR_LOGGING is named as such, because, the debug toolbar middleware
intercepts the logs, and affects the logging configured in the LOGGING setting. Therefore, this
name is used to show the tradeoff between both settings.
"""
if DEBUG is True and USE_DJANGO_DEBUG_TOOLBAR_FOR_LOGGING is True:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ['127.0.0.1']

if STREAM_BACKEND_LOGS_TO_CONSOLE is True:
    LOGGING['loggers']['django.db.backends']['handlers'].append('stream_default')