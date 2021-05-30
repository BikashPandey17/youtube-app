# Youtube App
```
TODO:
1. Add description of the project (along with system diagram)
2. Requirements for the project
3. Installing the requirements
4. Running the Application (Schedular, Celery worker, Gunicorn Workers)
```

## Folder Structure

```
.
├── Dockerfile
├── myapp
│   ├── config
│   │   ├── __base.py
│   │   ├── __dev.py
|   |   ├── .env (secret)
│   │   ├── __init__.py
│   │   └── __prod.py
│   ├── source
│   │   ├── celery_config.py
│   │   ├── celery_schedular.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   └── model.py
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── tasks.py
│   │   └── views.py
│   └── wsgi.py
├── README.md
└── requirements.txt
```


### Create a virtual environment

```python
pip install virtualenv

python -m virtualenv venv
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
source venv/bin/activate (windows: venv\Scripts\activate)
pip install -r requirements.txt
```
# Youtube Fetch Schedular

This module does the following jobs:

    1. Fetch youtube data for a fixed search query (every 4 minutes)
    2. Saves the youtube data in database

## Start Redis

    1. `redis-cli shutdown`
    2. `redis-server`

## Start Elastic search

```bash
./bin/elasticsearch
```

## Start celery-beat (schedular)

    `celery beat -A myapp.source.celery_schedular --loglevel=INFO`

## Start celery-worker

    In Windows: `celery worker -A myapp.source.celery -P solo --loglevel=INFO`
    In UNIX : `celery worker -A myapp.source.celery --loglevel=INFO`

# Youtube Search api

This module provides api for performing search on the youtube data

### To run the Flask server

#### Development server

```bash
set FLASK_APP=myapp.wsgi.py (linux : export FLASK_APP=myapp.wsgi.py)
flask run -h 0.0.0.0 -p 8091
```

#### Production server

```bash
gunicorn --workers=2 myapp.wsgi:app -b localhost:8091
```

## Docker commands

```bash
docker build --tag youtube-app .
docker run -d -p 8091:8091 --net="host" youtube-app
```
