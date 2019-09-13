from Pusher import xml_parser
from settings import XML_LINK, LATEST_POSTS_XML_PATH
import requests

if __name__ == '__main__':
    with open(LATEST_POSTS_XML_PATH, 'w') as file:
        file.write(requests.get(XML_LINK).text)
    with open(LATEST_POSTS_XML_PATH, 'r') as file:
        parser = xml_parser.ParserXml(file)
        posts = parser.get_posts()
        count = 0
        for post in posts:
            print(count)
            count += 1
            print(post.get('title'))
            print(post.get('link'))
            print(post.get('pubDate'))
