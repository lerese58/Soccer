from Pusher import utils

from pymongo import MongoClient

client = MongoClient('localhost', port=27018)  # standard port (27017) was already in use for some reason
db = client.pusher_database


def insert_new_posts(dev_mode=True):

    collection = db.posts
    posts = utils.get_posts()

    if dev_mode:
        post = posts[0]  # made not to overflow database
        collection.insert_one(post)

    else:
        for post in posts:
            collection.insert_one(post)


insert_new_posts()



