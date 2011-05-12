# Django settings for be_dal project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Thomas Gak Deluen', 'tgdn45@gmail.com'),
     ('David Leroy', 'davidleroy@noos.fr'),
     ('Axel Landeau', 'axel_landeau@gmail.com'),
)

MANAGERS = ADMINS

# SESSIONS
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_NAME = '_be-dal_sess'
CSRF_COOKIE_NAME = '_be-dal_csrf'

#DEFAULT_FROM_EMAIL = 'be-dal@be-dal.com'
EMAIL_SUBJECT_PREFIX = '[BE DAL]'

# LOGIN...
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/users/sign_in/'
LOGOUT_URL = '/users/sign_out/'

if DEBUG:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': 'db/db.db',                      # Or path to database file if using sqlite3.
          'USER': '',                      # Not used with sqlite3.
          'PASSWORD': '',                  # Not used with sqlite3.
          'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
      }
  }
else:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
          'NAME': '/home/be-dal/be_dal/db/db.db',                      # Or path to database file if using sqlite3.
          'USER': '',                      # Not used with sqlite3.
          'PASSWORD': '',                  # Not used with sqlite3.
          'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
          'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
      }
  }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if DEBUG:
  MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')
else:
  # use this for alwaysdata
  MEDIA_ROOT = '/home/be-dal/be_dal/public/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
# `SECRET_KEY` is hidden for security reasons,
# if you want to run the application, you'll need to generate one `SECRET_KEY`
# read README for help
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django_mobile.cache.middleware.CacheFlavourMiddleware',
)

ROOT_URLCONF = 'be_dal.urls'

TEMPLATE_DIRS = (
  os.path.join(os.path.dirname(__file__), '').replace('\\', '/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.contrib.messages.context_processors.messages',
  'django_mobile.context_processors.flavour',
  'django_mobile.context_processors.is_mobile',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'be_dal.rosetta',
    'be_dal.captcha',
    'be_dal.django_mobile',
    'be_dal._products',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
