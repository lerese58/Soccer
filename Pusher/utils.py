from Pusher import xml_parser, const

import re
import requests


def download_xml():
    with open('/home/lerese58/PycharmProjects/Soccer/latest_posts.xml', 'w') as file:
        page = requests.get(const.XML_LINK)
        file.write(page.text)
        return page.status_code


def build_message(post):
    message_text = f"*{post.get('title')}*\n\n" + f"{post.get('description')}" + f"\n\nLink: {post.get('link')}"
    return message_text


def get_tagged_posts():
    """
    :return: posts_list; each post already has all the tags as an attribute
    """
    with open('/home/lerese58/PycharmProjects/Soccer/latest_posts.xml', 'r') as file:
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
