import celery
from myapp.source import create_app
from myapp.config import Config
from myapp.source.celery_config import make_celery


app = create_app(Config)
celery = make_celery(app)

import myapp.source.tasks