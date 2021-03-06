
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%+!2ob33dtkpi#p2b_^^gk0jn#^6hv9oc4b#8=*=z)zzfd@25@'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']
DEBUG=True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'admin_auto_filters',
    'dbbackup',
    'yakuri.apps.YakuriConfig',
    'linebotpharm.apps.LinebotpharmConfig',
    'bootstrap4',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'pharmacology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['BASE_DIR','template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'yakuri.context.related',
                'django.template.context_processors.media',
            ],
            'builtins':[
                'bootstrap4.templatetags.bootstrap4',#bootstrap4???HTML????????????????????????
                ]
        },
    },
]

WSGI_APPLICATION = 'pharmacology.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

import dj_database_url
from dotenv import(find_dotenv,load_dotenv)

load_dotenv(find_dotenv())
DATABASES={
    'default':dj_database_url.config(conn_max_age=600)
}

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#?????????????????????????????????????????????
STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STRAGE='whitenoise.strage.CompressedManifestStaticFilesStrage'

#????????????????????????????????????????????????????????????
DBBACKUP_STORAGE='django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS={'location':os.path.join(BASE_DIR,'backups')}

#??????????????????????????????????????????

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

#??????????????????????????????ClOUDINARY???????????????????????????
CLOUDINARY_STORAGE={
    'CLOUD_NAME':'duipobhgk',
    'API_KEY':'742599664161793',
    'API_SECRET':'-QwM-l9ABp-mwNkyM-JBtuTfPEI',
            
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


