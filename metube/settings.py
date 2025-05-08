import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = (os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = (os.getenv('DEBUG'))

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'userauths',
    'channel',
    'useradmin',
    'import_export',
    'taggit',
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

ROOT_URLCONF = 'metube.urls'

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

WSGI_APPLICATION = 'metube.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': (os.getenv('ENGINE')),
        'NAME': (os.getenv('NAME')),
        'USER': (os.getenv('USER')),
        'PASSWORD': (os.getenv('PASSWORD')),
        'HOST': (os.getenv('HOST')),
        'PORT': (os.getenv('PORT')),
    }
}

# Password validation

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

LANGUAGE_CODE = (os.getenv('LANGUAGE_CODE'))
TIME_ZONE = (os.getenv('TIME_ZONE'))
USE_I18N = (os.getenv('USE_I18N'))
USE_L10N = (os.getenv('USE_L10N'))
USE_TZ = (os.getenv('USE_TZ'))

# Static files (CSS, JavaScript, Images)

STATIC_URL = (os.getenv('STATIC_URL'))
STATIC_ROOT = (os.getenv('STATIC_ROOT'))
STATICFILES_DIRS = (os.getenv('STATICFILES_DIRS'))

MEDIA_URL = (os.getenv('MEDIA_URL'))
MEDIA_ROOT = (os.getenv('MEDIA_ROOT'))

# Users

AUTH_USER_MODEL = (os.getenv('AUTH_USER_MODEL'))
LOGIN_URL = (os.getenv('LOGIN_URL'))

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin

JAZZMIN_SETTINGS = {
    'site_title': 'MeTube Admin',
    'site_header': 'MeTube',
    'site_brand': 'The Best or Nothing',
    'site_logo': 'images/logo.jpg',
    'login_logo': 'images/logo.jpg',
    'login_logo_dark': None,
    'site_logo_classes': 'img-circle',
    'site_icon': 'images/logo.jpg',
    'welcome_sign': 'Добро пожаловать на MeTube!',
    'copyright': 'MeTube Ltd',
    'search_model': ['auth.User', 'auth.Group'],
    'user_avatar': None,

    # Top Menu

    'topmenu_links': [
        {'name': 'Главная', 'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Техподдержка', 'url': '#', 'new_window': True},
        {'model': 'auth.User'},
        {'app': 'books'},
    ],

    # User Menu

    'usermenu_links': [
        {'name': 'Техподдержка', 'url': '#', 'new_window': True},
        {'model': 'auth.user'}
    ],

    # Side Menu

    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    'order_with_respect_to': ['auth', 'books', 'books.author', 'books.book'],
    'custom_links': {
        'books': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fas fa-comments',
            'permissions': ['books.view_book']
        }]
    },

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    # Related Modal

    'related_modal_active': False,

    # UI Tweaks

    'custom_css': None,
    'custom_js': None,
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,

    # Change view

    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {'auth.user': 'collapsible', 'auth.group': 'vertical_tabs'},
    'language_chooser': False,
}
