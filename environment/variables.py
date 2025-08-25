# from decouple import config
from decouple import config

class EnvironmentVariable:
    """
    @note: This class contains all the access data, common configuration variables
    that are used in this application.
    """
    # enc
    BACKEND_ENVIRONMENT = config('BACKEND_ENVIRONMENT')
    # jwt
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    # db
    DB_PORT = config('DB_PORT')
    DB_NAME = config('DB_NAME')
    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_HOST = config('DB_HOST')
    #aws
    AWS_S3_BASE_URL = config('AWS_S3_BASE_URL')
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_MEDIA_FOLDER = config('AWS_MEDIA_FOLDER')
    USE_S3_FOR_STATIC = config('USE_S3_FOR_STATIC')
    MIN_CONFIDENCE = config('MIN_CONFIDENCE')
    FLAGGED_KEYWORDS = config('FLAGGED_KEYWORDS')
    SENTIMENT_KEYWORDS = config('SENTIMENT_KEYWORDS')

