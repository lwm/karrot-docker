import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'db',
        'PASSWORD': 'db',
        'HOST': 'db',
        'PORT': '',
    }
}

SECRET_KEY = 'c*#4=n$s4!*gdgq3nora#a$*xznctg-6=4_edeg9^dsxk&=p=$'
DEBUG = True

# needed for deployment
STATIC_ROOT = './static/'
ALLOWED_HOSTS = ['*']

# Uploaded files location, e.g. user photos
MEDIA_ROOT = './uploads/'
MEDIA_URL = '/media/'

######
# Mail configuration
# Uses the console backend for local development
# Set the sparkpost key on deploy
######

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'maildev'


# ANYMAIL = {
#     "SPARKPOST_API_KEY": "your sparkpost key"
# }

DEFAULT_FROM_EMAIL = "fstool@yunity.org"  # can be anything if using the console backend
HOSTNAME = 'http://localhost:8080'  # for constructing the frontend URL
SITE_NAME = 'karrot.world' # used as human readable site name, for example in e-mail templates

 
######
# InfluxDB config for statistics reporting
# Disabled by default
######

INFLUXDB_DISABLED = False
INFLUXDB_HOST = 'influxdb'
INFLUXDB_PORT = '8086'
INFLUXDB_USER = ''
INFLUXDB_PASSWORD = ''
INFLUXDB_DATABASE = 'fstool'
INFLUXDB_TAGS_HOST = 'docker'
INFLUXDB_TIMEOUT = 2
INFLUXDB_USE_CELERY = False
INFLUXDB_USE_THREADING = True

######
# Firebase Cloud Messaging config
# For sending push messages
# Get one from https://console.firebase.google.com
######

FCM_SERVER_KEY = 'your server key'

#######
# Sentry.io config for error reporting
# Only needs to be enabled on deploy
########

# import os
# import raven

# RAVEN_CONFIG = {
#    'dsn': 'https://f4b3de91ad384e4ca0d371c591cf3904:60760787f4464c5293afa6fe877d3d9d@sentry.io/147126',
#    # If you are using git, you can also automatically configure the
#    # release based on the git info.
#    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
#}
