import json
from flask import current_app

from myapp.source import es_client
from myapp.source.models import Youtube
from myapp.source.search import search



@search.route('/', methods=['GET'])
def default():
    current_app.logger.info("OK")
    return "Server Up!"


@search.route('/search/title/<search_query>', methods=['GET'])
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


@search.route('/search/description/<search_query>', methods=['GET'])
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