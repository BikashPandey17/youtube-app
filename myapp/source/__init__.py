from flask import Flask
from flask_cors import CORS
from logging.config import dictConfig
from myapp.source.celery_config import make_celery

from myapp.config import CORS_ALLOWED, REDIS_URL

app = Flask(__name__)
flask_app_copy = app
cors = CORS(app, resources={r"/*": {"origins": CORS_ALLOWED}})
app.config["REDIS_URL"] = REDIS_URL
celery = make_celery(app)

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