import os
import time
import mongoengine

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_cluster = os.environ.get('DB_CLUSTER')

connection_string = f'mongodb+srv://{db_user}:{db_pass}@{db_cluster}.mongodb.net/test?retryWrites=true&w=majority'
mongoengine.connect('Soccer', host=connection_string)


class User(mongoengine.Document):
    chat_id = mongoengine.IntField(primary_key=True)
    preferred_time = mongoengine.IntField(default=0)


class Tag(mongoengine.Document):
    title = mongoengine.StringField(max_length=128, primary_key=True)
    users = mongoengine.ListField(mongoengine.ReferenceField(User))


class Message(mongoengine.Document):
    text = mongoengine.StringField(max_length=256, required=True)
    pub_date = mongoengine.IntField(required=True)
    tags = mongoengine.ListField(mongoengine.ReferenceField(Tag))


class Queue(mongoengine.Document):
    message = mongoengine.ReferenceField('Message')
    user = mongoengine.ReferenceField('User')
    timestamp = mongoengine.IntField(default=int(time.time()))
