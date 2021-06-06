import json
import traceback
from flask import current_app

from myapp.source.es_ops import search_query as sq
from myapp.source.models import Youtube
from myapp.source.search import search


@search.route('/', methods=['GET'])
def default():
    current_app.logger.info("OK")
    return {"data": "Server Up!"}, 200


@search.route('/search/title/<search_query>', methods=['GET'])
def search_title(search_query):
    try:
        body = {
            "size": 3,
            "from":0,
            "query": {
                "match": {
                    "title": str(search_query)
                }
            }
        }
        search_output = sq(body)
        data = []
        for hits in search_output['hits']['hits']:
            try:
                data.append(json.loads(Youtube.objects.get(video_id=hits['_id']).to_json()))
            except:
                continue
        return {"data": data}, 200
    except:
        traceback.print_exc()
        return {"data": []}, 500


@search.route('/search/description/<search_query>', methods=['GET'])
def search_description(search_query):
    try:
        body = {
            "query": {
                "match": {
                    "description": str(search_query)
                }
            }
        }
        search_output = sq(body)
        data = []
        for hits in search_output['hits']['hits']:
            try:
                data.append(json.loads(Youtube.objects.get(video_id=hits['_id']).to_json()))
            except:
                continue
        return {"data": data}, 200
    except:
        traceback.print_exc()
        return {"data": []}, 500
