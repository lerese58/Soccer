from Pusher import xml_parser, const

import re
import requests


def get_posts():

    """
    :return: posts_list; each post already has all the tags as an attribute
    """

    with open('latest_posts.xml', 'w') as file:
        file.write(requests.get(const.XML_LINK).text)

    with open('latest_posts.xml', 'r') as file:
        p = xml_parser.ParserXml(file)
        p.parse_xml()
        posts = p.get_posts()

        for post in posts:
            link = post.get('link')
            tags = get_tags_from_page(link)
            post['tags'] = tags

        return posts


def get_tags_from_page(url):

    """
    :return: if url.status_code == 200, returns list of lowercase tags
             else returns an empty list
    """

    div_pattern = r'<div class="news-item__tags-line"> Теги (.*)</div>'
    tag_name_pattern = r'.*?title="(.*?)"'

    page = requests.get(url)
    if page.status_code == 200:
        tags_div = re.findall(div_pattern, page.text)[0]
        tags = re.findall(tag_name_pattern, tags_div)
        tags_lower = []
        for tag in tags:
            tags_lower.append(tag.lower())
        return tags_lower
    else:
        return list()
