import json

from Pusher import utils
import settings

if __name__ == '__main__':
    if utils.download_xml() == 200:  # OK
        posts = utils.get_tagged_posts_from_xml()
        utils.make_json(posts, settings.LATEST_POSTS_JSON_PATH)
        with open(settings.LATEST_POSTS_JSON_PATH, 'r') as file:
            posts = json.load(file)
        print(posts)
    else:
        print("Error loading file")
