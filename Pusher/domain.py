from pymongo import MongoClient

client = MongoClient('localhost', port=27018)  # standard port (27017) was already in use for some reason
db = client.pusher_database


def insert_new_posts(posts: list):
    collection = db.posts
    collection.insert_many(posts)


def insert_new_posts_dev(posts: list):
    collection = db.posts
    post = posts[0]  # made not to overflow database
    collection.insert_one(post)


if __name__ == '__main__':
    insert_new_posts_dev()
