import re
import requests


def get_tags_from_page(url):

    """
    :return: if url.status_code == 200, returns list of lowercase tags
             else returns an empty list
    """

    pattern = r'<div class="news-item__tags-line"> Теги (.*)</div>'
    patton = r'.*?title="(.*?)"'

    page = requests.get(url)
    if page.status_code == 200:
        tags_div = re.findall(pattern, page.text)[0]
        tags = re.findall(patton, tags_div)
        tags_lower = []
        for tag in tags:
            tags_lower.append(tag.lower())
        return tags_lower
    else:
        return list()
