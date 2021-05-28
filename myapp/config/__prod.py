import os

# Celery
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") 

# Redis
REDIS_URL = os.environ.get("REDIS_URL") 
REDIS_PORT = os.environ.get("REDIS_URL") 

# cors policy
CORS_ALLOWED = ["*"]