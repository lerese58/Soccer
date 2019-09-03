from Pusher import xml_parser, const

import re
import requests


def pull_posts(posts_file='latest_posts.xml'):
    print(download_xml(posts_file))
    return get_tagged_posts(posts_file)


def download_xml(posts_file='latest_posts.xml'):
    """
    :return: 200 in case everything is fine
    """
    with open(posts_file, 'w') as file:
        page = requests.get(const.XML_LINK)
        file.write(page.text)
        return page.status_code


def get_tagged_posts(posts_file='latest_posts.xml'):
    """
    :return: posts_list; each post already has all the tags as an attribute
    """
    with open(posts_file, 'r') as file:
        parser = xml_parser.ParserXml(file)
        posts = parser.get_posts()
        for post in posts:
            page_url = post['link']
            tags = get_tags_from_page(page_url)
            post['tags'] = tags
        return posts


def get_tags_from_page(url):
    """
    :return: list of found lowercase tags
    """
    div_pattern = r'<div class="news-item__tags-line"> Теги (.*)</div>'
    tag_name_pattern = r'.*?title="(.*?)"'

    page = requests.get(url)
    tags_div = re.findall(div_pattern, page.text)[0]
    tags = re.findall(tag_name_pattern, tags_div)
    tags_lower = []
    for tag in tags:
        tags_lower.append(tag.lower())
    return tags_lower
