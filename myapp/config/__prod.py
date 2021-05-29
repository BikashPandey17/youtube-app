import os
from .__base import *

DEBUG = False
# youtube api key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") 

# Redis
REDIS_URL = os.environ.get("REDIS_URL") 
REDIS_PORT = os.environ.get("REDIS_URL") 

# cors policy
CORS_ALLOWED = ["*"]

# mongo cred
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# elastic search 
ES_HOST = os.environ.get('ES_HOST')
ES_PORT = int(os.environ.get('ES_PORT'))