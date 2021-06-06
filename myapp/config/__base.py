import os

class BaseConfig():
    # App Configs:
    SECRET_KEY = os.environ.get("SECRET_KEY").encode("utf-8")

    # DATABASE AND COLLECTIONS
    DATABASE = "Data"

    # elastic search 
    ES_INDEX = "yt_data"
