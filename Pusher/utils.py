from Pusher import xml_parser
from settings import LATEST_POSTS_XML_PATH, XML_LINK

import re
import requests
import json

from datetime import datetime


def get_posts(xml_path=LATEST_POSTS_XML_PATH):
    """
    Downloads xml,
    :return:
    """
    status = download_xml(xml_path)
    if status == 200:
        print("xml file successfully downloaded")
    else:
        print(f"xml.status_code == {status}")

    posts = get_tagged_posts_from_xml(xml_path)
    return posts


def download_xml(xml_path=LATEST_POSTS_XML_PATH):
    with open(xml_path, 'w') as file:
        page = requests.get(XML_LINK)
        file.write(page.text)
        print(f"xml downloaded with code {page.status_code}")
        return page.status_code


def make_json(obj, path):
    with open(path, 'w') as file:
        json.dump(obj, file, ensure_ascii=False)


def get_tagged_posts_from_xml(xml_path=LATEST_POSTS_XML_PATH):
    """
    :return: posts_list; each post already has all the tags as an attribute
    """
    with open(xml_path, 'r') as file:
        parser = xml_parser.ParserXml(file)
        posts = parser.get_posts()
        print("parsed")
        for post in posts:
            page_url = post['link']
            tags = get_tags_from_page(page_url)
            post['tags'] = tags
        print("posts are ready")
        return posts


def get_tags_from_page(url):
    """
    :return: list of found lowercase tags
    """
    div_pattern = r'<div class="news-item__tags-line"> Теги (.*)</div>'
    tag_name_pattern = r'.*?title="(.*?)"'
    print(f'starting getting tags from {url}')
    page = requests.get(url)
    tags_div = re.findall(div_pattern, page.text)[0]
    tags = re.findall(tag_name_pattern, tags_div)
    tags_lower = []
    for tag in tags:
        tags_lower.append(tag.lower())
    print(f'finished getting tags from {url}')
    return tags_lower


def datetime_from(str_date):
    return datetime.strptime(str_date[:-6], "%a, %d %b %Y %H:%M:%S")
