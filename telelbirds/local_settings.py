from .settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = '79&vz)($@07na+25vw4nb0r^p*6w0j+-x!m)y5p#76tp!gvs_5'

# 3rd-party apps tracking IDs.
INTERCOM_APP_ID = None
GOOGLE_ANALYTICS_TRACKING_ID = None
ADDTHIS_PUBLISHER_ID = None

ADMINS = (
    ('Local Admin', 'admin@telelbirds.com'),
)

MANAGERS = ADMINS

CONTACTS = {
    'support_email': 'support@telelbirds.com',
    'admin_email': 'admin@telelbirds.com',
    'info_email': 'info@telelbirds.com',
}

# For 'subscribers' app
SEND_SUBSCRIBERS_EMAIL_CONFIRMATION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'telel_birds',
        'USER': 'telel',
        'PASSWORD': 'pw4telel',
        'HOST': os.getenv('POSTGRESQL_HOST', 'localhost'),
        'PORT': '',
    }
}