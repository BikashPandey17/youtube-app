import json
import traceback
from flask import current_app, request

from myapp.source.es_ops import search_query as sq
from myapp.source.models import Youtube
from myapp.source.search import search


@search.route('/', methods=['GET'])
def default():
    current_app.logger.info("OK")
    return {"data": "Server Up!"}, 200


@search.route('/search/title', methods=['GET'])
def search_title():
    try:
        search_query = request.args.get('q', "")
        body = {
            "size": request.args.get('size',3),
            "from": request.args.get('from',0),
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
        return {"data": data, "total_results":search_output["hits"]["total"]}, 200
    except:
        traceback.print_exc()
        return {"data": []}, 500


@search.route('/search/description', methods=['GET'])
def search_description():
    try:
        search_query = request.args.get('q', "")
        body = {
            "size": request.args.get('size',3),
            "from": request.args.get('from',0),
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
        return {"data": data, "total_results":search_output["hits"]["total"]}, 200
    except:
        traceback.print_exc()
        return {"data": [], "total_results":{}}, 500


@search.route('/search', methods=['GET'])
def search_all():
    try:
        search_query = request.args.get('q')
        print(search_query)
        body = {
            "size": request.args.get('size',3),
            "from": request.args.get('from',0),
            "query": {
                "multi_match": {
                    "query": request.args.get('q'),
                    "fields": ["description", "title"]
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
        return {"data": data, "total_results":search_output["hits"]["total"]}, 200
    except:
        traceback.print_exc()
        return {"data": [], "total_results":{}}, 500


@search.route('/list', methods=['GET'])
def list_all():
    try:
        page = int(request.args.get('page', 0))
        size = int(request.args.get('size', 3))

        offset = (page - 0) * size

        data = json.loads(Youtube.objects.order_by('-published_at').skip( offset ).limit( size ).to_json())
        return {"data": data, "total_results":{"value":Youtube.objects().count()}}, 200
    except:
        traceback.print_exc()
        return {"data": [], "total_results":{}}, 500
