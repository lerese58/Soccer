import xml.etree.cElementTree as et


class ParserXml:

    def __init__(self, xml_file_path, xml_root=None):
        self.file = xml_file_path
        self.root = xml_root

    def parse_xml(self):
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
        return posts
