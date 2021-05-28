from celery.schedules import crontab
from myapp.source import celery

celery.conf.timezone = 'UTC'


celery.conf.beat_schedule = {
    'fetch_emails': {
        'task': 'source.tasks.fetch_youtube_videos',
        # Every 1 minute
        'schedule': crontab(minute="*")
    }
}