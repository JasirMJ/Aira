"""
Django settings for Aira project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b#1&i-^mj(o*or&c&l35jikrl_gob_uo&mrbs@0(8kf=y8=25g'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = [
    '192.168.0.104',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_mysql',
    'rest_framework',
    'AiraPanel',
    'product',
    'billing',
    'invoice',

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

ROOT_URLCONF = 'Aira.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Aira.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#
# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         },
#     }
# else:
#     DATABASES = {
#         # 'default': {
#         #     'ENGINE': 'django.db.backends.sqlite3',
#         #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         # },
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'USER':'root',                          #msql user name
#             'PASSWORD':'',                          #msql password
#             'NAME':'aira',                     #dbname
#             'HOST':'localhost',
#             'PORT':'3306',
#             'OPTIONS': {
#                 # 'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
#                 'init_command':'SET innodb_strict_mode=1',
#                 #tell MYSQLdb to connect with 'utf8mb4' character set
#                 'charset':'utf8mb4',
#             },
#         }
#     }

DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # },
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER':'root',                          #msql user name
            'PASSWORD':'',                          #msql password
            'NAME':'aira',                     #dbname
            'HOST':'localhost',
            'PORT':'3306',
            'OPTIONS': {
                # 'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
                'init_command':'SET innodb_strict_mode=1',
                #tell MYSQLdb to connect with 'utf8mb4' character set
                'charset':'utf8mb4',
            },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
}

# '''/Sendgrid'''
#
# # SENDGRID_API_KEY = "Bearer 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"
#
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# # SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
# SENDGRID_API_KEY = "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"
# SENDGRID_SANDBOX_MODE_IN_DEBUG=False
# '''Sendgrid/'''

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}