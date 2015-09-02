"""
Django settings for pasteque_admin project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# This is a dummy key, only used in developpement
SECRET_KEY = 'y=#!(+pw(1$m9h2+lv&x6(+zd!3x6uj32$+wc$f_u+(4n#c1p9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wordpress_auth_lite',
    'wordpress_db',
    'dummy',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wordpress_auth_lite.middleware.WordPressAuthMiddleware', # django-wordpress-auth-lite
)

ROOT_URLCONF = 'pasteque_admin.urls'

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

WSGI_APPLICATION = 'pasteque_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # django-wordpress-auth-lite, replace fields with your own settings
    'wordpress': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pasteque_master_wp',
        'USER': 'pasteque',
        'PASSWORD': 'pasteque',
        'HOST': 'localhost',
        'PORT': 3306,
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# django-wordpress-auth-lite
# dummy keys, replace by your wordpress keys (in wp-config.php)
WORDPRESS_LOGGED_IN_KEY = 'Io@|5Mq`Vkd$|BtXRD%S9uS,+ib6[VqVVmp|fji>^nx1!+pX]a@z?@=z[z(u-qcE'
WORDPRESS_LOGGED_IN_SALT = 'hD[qi3.[b5;j!Mk-P|#%55 arulz7h5|#sk5}vPM;tw}){^^@1YCj:=-%W]`|Z%$'

# worpress_db app
# replace by the table of the wordpress db that contains pasteque's users
WORDPRESS_PT_USER_TABLE = 'wp_pasteque'
