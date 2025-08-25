from urllib.parse import urlparse

from .base import *
from environment.variables import EnvironmentVariable

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': EnvironmentVariable.DB_NAME,
        'USER': EnvironmentVariable.DB_USER,
        'PASSWORD': EnvironmentVariable.DB_PASSWORD,
        'HOST': EnvironmentVariable.DB_HOST,
        'PORT': EnvironmentVariable.DB_PORT,
    }
}


LOGGING_CONFIG = None

ALLOWED_HOSTS = [
    '*',
    '35.92.226.26',
    'localhost', '127.0.0.1'  # Localhost
    # 'backend.crrms.dataterrain-dev.net',
]



USE_X_FORWARDED_HOST = True

# jwt
JWT_SECRET_KEY = EnvironmentVariable.JWT_SECRET_KEY
JWT_ALGORITHM = "HS256"


LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True

#aws
AWS_S3_BASE_URL = EnvironmentVariable.AWS_S3_BASE_URL
AWS_S3_CUSTOM_DOMAIN = urlparse(AWS_S3_BASE_URL).hostname
AWS_S3_REGION_NAME = EnvironmentVariable.AWS_S3_REGION_NAME
AWS_ACCESS_KEY_ID = EnvironmentVariable.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = EnvironmentVariable.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = EnvironmentVariable.AWS_STORAGE_BUCKET_NAME
AWS_MEDIA_FOLDER = EnvironmentVariable.AWS_MEDIA_FOLDER
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_QUERYSTRING_EXPIRE = '604800'
AWS_LOCATION = 'static'
MIN_CONFIDENCE = EnvironmentVariable.MIN_CONFIDENCE
FLAGGED_KEYWORDS = EnvironmentVariable.FLAGGED_KEYWORDS
SENTIMENT_KEYWORDS = EnvironmentVariable.SENTIMENT_KEYWORDS