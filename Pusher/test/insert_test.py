from Pusher import utils

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost', port=27018)  # standard port (27017) was already in use for some reason
    db = client.pusher_database
    collection = db.posts
    posts = utils.get_tagged_posts_from_xml()
    print(collection.insert_many(posts))
    print(len(posts))
