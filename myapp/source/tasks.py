import datetime
import json

from myapp.source import app, celery


# TODO: If that email exists do not save that email
@celery.task(name="source.tasks.fetch_youtube_videos")
def fetch_youtube_videos():
    app.logger.info(
        f"This task is being executed at :{datetime.datetime.utcnow()}")
