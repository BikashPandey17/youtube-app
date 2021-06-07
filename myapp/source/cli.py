import json
import traceback

from myapp.config import Config
from myapp.source.es_ops import es_connect
from myapp.source.models import Youtube

def reindex():
    try:
        status, es_client = es_connect()
        if not status:
            return False
        # delete the exisitng index
        es_client.indices.delete(index=Config.ES_INDEX)
        # create an new index
        es_client.indices.create(index=Config.ES_INDEX)
        # insert the documents in the mongodb as index
        list_of_docs = json.loads(Youtube.objects().to_json())
        from pprint import pprint
        for doc in list_of_docs:
            doc_to_insert = {
                "title": doc['snippet']['title'],
                "description": doc['snippet']['description'],
            }
            es_client.index(index=Config.ES_INDEX, doc_type="video", id=doc['video_id'], body=doc_to_insert)
        return True
    except:
        traceback.print_exc()
        return False
    finally:
        es_client.transport.close()