from flask import Flask
from flask_cors import CORS
from logging.config import dictConfig
from myapp.source.celery_config import make_celery
from googleapiclient.discovery import build
from elasticsearch import Elasticsearch

from myapp.config import (CORS_ALLOWED, REDIS_URL, YOUTUBE_API_KEY,
                          ES_HOST, ES_PORT, DATABASE, DB_HOST, DB_PORT, ES_INDEX)
from myapp.source.database import initialize_db

app = Flask(__name__)
flask_app_copy = app
cors = CORS(app, resources={r"/*": {"origins": CORS_ALLOWED}})
app.config["REDIS_URL"] = REDIS_URL
app.config['MONGODB_SETTINGS'] = {
    'db': DATABASE,
    'host': DB_HOST,
    'port': DB_PORT
}
celery = make_celery(app)
initialize_db(app)
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
es_client = Elasticsearch(HOST=ES_HOST, PORT=ES_PORT)
if not es_client.indices.exists(index=ES_INDEX):
    es_client.indices.create(index=ES_INDEX)


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s]|%(levelname)s|%(process)s, %(processName)s|%(thread)s, %(threadName)s|%(module)s|%(funcName)s|%(lineno)s|%(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

import myapp.source.tasks 
from myapp.source.routes import *
