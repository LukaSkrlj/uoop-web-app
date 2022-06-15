"""
Django settings for uoop project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
import os
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-775%nclb2iji+!(v@+ybb_ss!r2w5w9ul6rshn8qix)6@c89df'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',
    'app_cms_integration',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'django_ace',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'markdownify.apps.MarkdownifyConfig',
]
    

# if DEBUG:
#     INSTALLED_APPS += ('mockdjangosaml2',)
# else:
#     INSTALLED_APPS += ('djangosaml2',)

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'uoop.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'uoop.wsgi.application'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# AUTHENTICATION_BACKENDS = (
#     'djangosaml2.backends.Saml2Backend',
# )

SAML_CREATE_UNKNOWN_USER = False

SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'username'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SAML_ATTRIBUTE_MAPPING = {
    'hrEduPersonUniqueID': ('username', ),
    'mail': ('email', ),
    'givenName': ('first_name', ),
    'sn': ('last_name', ),
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# STATICFILES_FINDERS = [
#     'compressor.finders.CompressorFinder'
# ]

# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'django_libsass.SassCompiler'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MOCK_SAML2_USERS = {
    'admin@aai-test.hr': {
        'password': 'admin',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['admin@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Admin Surname'],
                'hrEduPersonOIB': ['12345678901'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['admin.surname@aai-test.hr'],
                'givenName': ['Admin']
            },
        },
    },
    'employee@aai-test.hr': {
        'password': 'somepwd1',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['employee@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['djelatnik'],
                'cn': ['Employee Surname'],
                'hrEduPersonOIB': ['12345678902'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['employee.surname@aai-test.hr'],
                'givenName': ['Employee']
            },
        },
    },
    'student@aai-test.hr': {
        'password': 'somepwd2',
        'session_info': {
            'ava': {
                'hrEduPersonUniqueID': ['student@aai-test.hr'],
                'hrEduPersonPrimaryAffiliation': ['student'],
                'cn': ['Student Surname'],
                'hrEduPersonOIB': ['12345678903'],
                'sn': ['Surname'],
                'hrEduPersonHomeOrg': ['aai-test.hr'],
                'mail': ['student.surname@aai-test.hr'],
                'givenName': ['Student']
            },
        },
    },
}

LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
    ('osustavu.html', 'O sustavu')
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

CMS_TEMPLATE_INHERITANCE = False