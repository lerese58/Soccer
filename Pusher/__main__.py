import json

from Pusher import domain, utils
from Puller import const

if __name__ == '__main__':
    if utils.download_xml() == 200:  # OK
        posts = utils.get_tagged_posts_from_xml()
        utils.make_json(posts, const.LATEST_POSTS_PATH)
        with open(const.LATEST_POSTS_PATH, 'r') as file:
            posts = json.load(file)
        print(posts)
    else:
        print("Error loading file")
