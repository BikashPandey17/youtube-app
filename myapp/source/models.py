from myapp.source import db

class Youtube(db.DynamicDocument):
    video_id = db.StringField(required=True, unique=True)
    meta = {
        'collection': 'youtube',
        'indexes': [
            'video_id'
        ]
    }
