"""
Django 4.1.7
"""
import os
import environ
import psycopg2
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# set STAGE based on environment variable
STAGE = env('STAGE')

# Determine database settings based on STAGE
if STAGE == 'production':
    DATABASES = {
        'default': {
            'ENGINE': env('PROD_DB_ENGINE'),
            'NAME': env('PROD_DB_NAME'),
            'USER': env('PROD_DB_USER'),
            'PASSWORD': env('PROD_DB_PASSWORD'),
            'HOST': env('PROD_DB_HOST'),
            'PORT': env('PROD_DB_PORT'),
        }
    }
    SECRET_KEY = env('PROD_SECRET_KEY')
    DEBUG = False
    ALLOWED_HOSTS = env.list('PROD_ALLOWED_HOSTS')
elif STAGE == 'development':
    DATABASES = {
        'default': {
            'ENGINE': env('DEV_DB_ENGINE'),
            'NAME': env('DEV_DB_NAME'),
            'USER': env('DEV_DB_USER'),
            'PASSWORD': env('DEV_DB_PASSWORD'),
            'HOST': env('DEV_DB_HOST'),
            'PORT': env('DEV_DB_PORT'),
        }
    }
    SECRET_KEY = env('DEV_SECRET_KEY')
    DEBUG = True
    ALLOWED_HOSTS = env.list('DEV_ALLOWED_HOSTS')
else:
    raise ValueError('Invalid STAGE value')


# Application definition
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    'whitenoise',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'board.apps.BoardConfig',
    'drf_yasg',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_simplejwt.token_blacklist',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rewardo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'board', 'templates', 'board'),
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

WSGI_APPLICATION = 'rewardo.wsgi.application'

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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/js'),
    os.path.join(BASE_DIR, 'static/css'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jet Dashboard
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Authentication backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# email backend
# outputs email message to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': (
        'rest_framework.schemas.coreapi.AutoSchema',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_GENERATOR_CLASS': 'drf_yasg.generators.OpenAPISchemaGenerator',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}


# Enable the toolbar only for development
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = [
        '127.0.0.1',
    ]

    # Set the path to the debug toolbar's URL configuration
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
        'RESULTS_CACHE_SIZE': 3,
        'SHOW_COLLAPSED': True,
    }

    # Set the path to the debug toolbar's static files
    STATICFILES_DIRS += [
        os.path.join(BASE_DIR, 'debug_toolbar', 'static'),
    ]

# serve this url instead of /    
#FORCE_SCRIPT_NAME = '/api/v1'

CSRF_COOKIE_SECURE=True