import json

from app.Pusher import utils
from app import config

if __name__ == '__main__':
    with open(config.LATEST_POSTS_JSON_PATH, 'r') as file:
        posts: list = json.load(file)
    last_post_from_json = posts[0]
    last_post_time = utils.datetime_from(last_post_from_json.get('pubDate'))

    print(f"PubDate of the last post in json is {last_post_time}")
    print(f"The post is: {last_post_from_json.get('title')}")

    if utils.download_xml() == 200:  # OK
        downloaded_posts = utils.get_tagged_posts_from_xml()
        new_posts = [p for p in downloaded_posts if utils.datetime_from(p.get('pubDate')) > last_post_time]
        posts = new_posts + posts  # order is important
        utils.make_json(posts, config.LATEST_POSTS_JSON_PATH)
        print(new_posts or "No new posts found")
    else:
        print("Error loading file")
