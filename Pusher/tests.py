from Pusher import xml_parser
import requests

xml_link = 'https://www.sports.ru/rss/rubric.xml?s=208'


def get_posts():
    with open('example.xml', 'w') as file:
        file.write(requests.get(xml_link).text)

    with open('example.xml', 'r') as file:
        p = xml_parser.ParserXml(file)
        p.parse_xml()
        posts = p.get_posts()
        count = 0
        for post in posts:
            print(count)
            count += 1
            print(post.get('title'))
            print(post.get('link'))


get_posts()
