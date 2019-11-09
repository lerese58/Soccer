import xml.etree.cElementTree as et
import re


class ParserXml:

    def __init__(self, xml_file_path):
        self.file = xml_file_path
        tree = et.ElementTree(file=self.file)
        self.root = tree.getroot()

    def get_posts(self):
        posts = []
        for elem in self.root:
            for item_elem in elem.findall("item"):
                post = {}
                for field in item_elem.getchildren():
                    post[field.tag] = field.text
                posts.append(post)
        posts = filter_out_ads(posts)
        return posts


def filter_out_ads(items: list) -> list:
    return [p for p in items if re.match(r'https://www\.sports\.ru/football/[0-9]+\.html', p.get('link')) is not None]
