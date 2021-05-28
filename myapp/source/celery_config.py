from celery import Celery
from myapp.config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=CELERY_RESULT_BACKEND,
        broker=CELERY_BROKER_URL
    )
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery