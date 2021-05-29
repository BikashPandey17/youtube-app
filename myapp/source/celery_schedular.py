from myapp.source import celery
from datetime import timedelta

celery.conf.timezone = 'UTC'


celery.conf.beat_schedule = {
    'fetch_emails': {
        'task': 'source.tasks.fetch_youtube_videos',
        # Every 10 seconds
        'schedule': timedelta(seconds=10)
    }
}