"""
This file is dedicated to perform
Elastic search operations for the application
"""

import json
import traceback
from elasticsearch import Elasticsearch

from myapp.config import Config

def es_connect():
    try:
        es_client = Elasticsearch(HOST=Config.ES_HOST, PORT=Config.ES_PORT)
        return True, es_client
    except:
        return False, None

def search_query(query: dict):
    try:
        status, es_client = es_connect()
        if not status:
            return {}
        search_output = es_client.search(index=Config.ES_INDEX, body=query)
        return search_output
    except:
        traceback.print_exc()
        return {}
    finally:
        es_client.transport.close()

def create_index():
    try:
        status, es_client = es_connect()
        if not status:
            return False
        if not es_client.indices.exists(index=Config.ES_INDEX):
            es_client.indices.create(index=Config.ES_INDEX)
        pass
    except:
        traceback.print_exc()
        return False
    finally:
        es_client.transport.close()

def insert_index(id: str, data: dict):
    try:
        status, es_client = es_connect()
        if not status:
            return False
        es_client.index(index=Config.ES_INDEX, doc_type="video", id=id, body=data)
        return True
    except:
        traceback.print_exc()
        return False
    finally:
        es_client.transport.close()
