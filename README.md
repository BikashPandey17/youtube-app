# Youtube App

## Project Goal

To make a System that fetches recently uploaded videos (related to a fixed keyword) and exposes the videos for search in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

Here's an Architechure diagram of the application

![Application Architecture](/yt-app-arch.png)

## Basic Specifications:

1. We should have a background schedular running at an interval (of say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos in a database with proper indexes.

2. A GET API which returns the stored video data in a paginated response sorted in descending order os published datetime.

3. A basic search API to search the stored videos using their title and description in paginated fashion.

4. Dockerize the Project. (preferably docker compose to include redis and elaticsearch)

5. It should be scalable and optimized.

## Folder Structure

```
.
├── Dockerfile
├── myapp
│   ├── celery_schedular.py
│   ├── celery_worker.py
│   ├── config
│   │   ├── __base.py
│   │   ├── __dev.py
|   |   ├── .env (secret)
│   │   ├── __init__.py
│   │   └── __prod.py
│   ├── source
│   │   ├── celery_config.py
│   │   ├── cli.py
│   │   ├── es_ops.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── search
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   └── tasks.py
│   └── wsgi.py
├── README.md
├── requirements.txt
├── supervisord.conf
├── tests
│   ├── __init__.py
│   ├── test_basic.py
│   └── test_search.py
└── yt-app-arch.png
```

## Installing Requirements

Using a virtualenv is preferred

1. Python and pip (requirements.txt)
2. Redis
3. ElasticSearch
4. MongoDB

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

    `celery beat -A myapp.celery_schedular --loglevel=INFO`

## Start celery-worker

    In Windows: `celery worker -A myapp.celery_worker.celery -P solo --loglevel=INFO`
    In UNIX : `celery worker -A myapp.celery_worker.celery --loglevel=INFO`

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
