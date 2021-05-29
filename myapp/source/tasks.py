import datetime
import json
from mongoengine.errors import NotUniqueError
from myapp import source

from myapp.source import (app, celery, youtube, es_client)
from myapp.config import ES_INDEX
from myapp.source.database.model import Youtube



# TODO: If that email exists do not save that email
@celery.task(name="source.tasks.fetch_youtube_videos")
def fetch_youtube_videos():
    app.logger.info(
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
            es_client.index(index=ES_INDEX, doc_type="video", id=str(data['video_id']), body=doc_to_insert)
            print(doc_to_insert)
    return True
