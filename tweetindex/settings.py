from os.path import dirname, realpath
import django

# Calculated paths for django and the site
# Used as starting points for various other paths
DJANGO_ROOT = dirname(realpath(django.__file__))
SITE_ROOT = dirname(realpath(__file__))

SECRET_KEY = '-z^y45gxjt2rrrynj&hafaaca*y8n^xzc4g@9x^=@29hceg2y_'
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['localhost']

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'db',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tweetindex.urls'
WSGI_APPLICATION = 'tweetindex.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'tweetIndex',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
