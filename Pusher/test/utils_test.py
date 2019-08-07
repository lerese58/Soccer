from Pusher import xml_parser, const
import requests

if __name__ == '__main__':
    with open('latest_posts.xml', 'w') as file:
        file.write(requests.get(const.XML_LINK).text)
    with open('latest_posts.xml', 'r') as file:
        parser = xml_parser.ParserXml(file)
        posts = parser.get_posts()
        count = 0
        for post in posts:
            print(count)
            count += 1
            print(post.get('title'))
            print(post.get('link'))
            print(post.get('pubDate'))
