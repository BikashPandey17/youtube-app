from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from elasticsearch import Elasticsearch
from googleapiclient.discovery import build

from myapp.config import Config
from myapp.source.es_ops import create_index

db = MongoEngine()
cors = CORS()
youtube = build('youtube', 'v3', developerKey=Config.YOUTUBE_API_KEY)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": Config.CORS_ALLOWED}})

    create_index()

    from .search import search as search_blueprint
    app.register_blueprint(search_blueprint)

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
    return app
