import pymongo
import os
import datetime
import ssl

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_cluster = os.environ.get('DB_CLUSTER')

connection_string = f'mongodb+srv://{db_user}:{db_pass}@{db_cluster}.mongodb.net/test?retryWrites=true&w=majority'

client = pymongo.MongoClient(connection_string,
                             ssl=True,
                             ssl_cert_reqs=ssl.CERT_NONE)

db = client.soccer

posts = db.posts

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}


if __name__ == '__main__':
    print(connection_string)
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
