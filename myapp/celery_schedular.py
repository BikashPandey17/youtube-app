from myapp.celery_worker import celery
from datetime import timedelta

celery.conf.timezone = 'UTC'


celery.conf.beat_schedule = {
    'fetch_youtube_videos': {
        'task': 'source.tasks.fetch_youtube_videos',
        # Every 10 seconds
        'schedule': timedelta(seconds=10)
    }
}