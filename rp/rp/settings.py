# -*- coding: utf-8 -*-

import os
from .utils import glob_list


#
# Basic
# =================================================================================================
SITE_NAME = os.environ['SITE_NAME']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'rw-ai_6g&h3v8h1+y+ov238#0b5&c+u_!n0e@^+6e^0+g2_ci4'
DEBUG = True
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = glob_list(['127.0.0.1', '192.168.*.*', '172.*.*.*', '10.*.*.*'])
ROOT_URLCONF = 'rp.urls'
WSGI_APPLICATION = 'rp.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'mozilla_django_oidc',
    'rp.home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


#
# Templates
# =================================================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'rp/templates')],
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


#
# Databases
# =================================================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/data/db.sqlite3',
    }
}


#
# Authentication
# =================================================================================================
AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
AUTHENTICATION_BACKENDS = (
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = 'oidc_authentication_init'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'http://op.local/'
LOGIN_REDIRECT_URL_FAILURE = '/login-failed'


#
# Localization
# =================================================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#
# Logging
# =================================================================================================
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    },
}


#
# Storage
# =================================================================================================
STATIC_URL = '/static/'


#
# OpenID Connect
# =================================================================================================
OIDC_RP_CLIENT_ID = os.environ['OPENID_CLIEND_ID']
OIDC_RP_CLIENT_SECRET = os.environ['OPENID_CLIENT_SECRET']
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_CREATE_USER = True
OIDC_OP_BASE_URI = os.environ['OPENID_PROVIDER_URI']
OIDC_OP_AUTHORIZATION_ENDPOINT = OIDC_OP_BASE_URI + '/openid/authorize/'
OIDC_OP_TOKEN_ENDPOINT = OIDC_OP_BASE_URI + '/openid/token/'
OIDC_OP_USER_ENDPOINT = OIDC_OP_BASE_URI + '/openid/userinfo/'
OIDC_OP_JWKS_ENDPOINT = OIDC_OP_BASE_URI + '/openid/jwks/'
OIDC_OP_LOGOUT_ENDPOINT = OIDC_OP_BASE_URI + '/logout/'
OIDC_OP_LOGOUT_URL_METHOD = 'rp.openid.get_op_logout_url'
