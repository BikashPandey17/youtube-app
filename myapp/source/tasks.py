import datetime
import json
from mongoengine.errors import NotUniqueError
from flask import current_app

from myapp.source import (youtube, es_client)
from myapp.celery_worker import celery
from myapp.config import Config
from myapp.source.models import Youtube



@celery.task(name="source.tasks.fetch_youtube_videos")
def fetch_youtube_videos():
    current_app.logger.info(
        f"This task is being executed at :{datetime.datetime.utcnow()}")
    publishedAfter = datetime.datetime.now(datetime.timezone.utc).astimezone() - datetime.timedelta(minutes=4)
    request = youtube.search().list(
        part="snippet",
        order="date",
        publishedAfter=publishedAfter.isoformat(),
        q="covid",
        type="video"
    )
    response = request.execute()
    if response['items']:
        for data in response['items']:
            data['video_id'] = data['id']['videoId']
            del data['id']
            try:
                Youtube(**data).save()
            except NotUniqueError:
                continue
            doc_to_insert = {
                "title": data['snippet']['title'],
                "description": data['snippet']['description'],
            }
            es_client.index(index=Config.ES_INDEX, doc_type="video", id=str(data['video_id']), body=doc_to_insert)
            print(doc_to_insert)
    return True
