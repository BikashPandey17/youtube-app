import json

from myapp.config import ES_INDEX
from myapp.source import app, es_client
from myapp.source.database.model import Youtube


def default():
    app.logger.info("OK")
    return "Server Up!"

def search_title(search_query):
    body = {
        "query": {
            "match": {
                "title": str(search_query)
            }
        }
    }
    search_output = es_client.search(index="yt_data", body=body)
    resp = [json.loads(Youtube.objects.get(video_id=data['_id']).to_json()) for data in search_output['hits']['hits']]
    return { "data": resp }, 200
    
def search_description(search_query):
    body = {
        "query": {
            "match": {
                "description": str(search_query)
            }
        }
    }
    search_output = es_client.search(index="yt_data", body=body)
    resp = [json.loads(Youtube.objects.get(video_id=data['_id']).to_json()) for data in search_output['hits']['hits']]
    return { "data": resp }, 200