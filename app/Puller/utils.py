from app.config import USERS_PATH, LATEST_POSTS_JSON_PATH
import json


def get_posts_for(tags: list):
    print("collecting posts...")
    posts = decode_json(LATEST_POSTS_JSON_PATH)
    posts_for_message = []
    for tag in tags:
        for post in posts:
            if tag in post.get('tags'):
                posts_for_message.append(post)
    print(f'len of posts set = {len(posts_for_message)}')
    return posts_for_message


def decode_json(path: str):
    with open(path, 'r') as file:
        return json.load(file)


def get_tags_for(chat_id):
    print(f"collecting tags for {chat_id}")
    users_tags = decode_json(USERS_PATH)
    if users_tags.get(str(chat_id)) is not None:
        print(f"count of tags for {chat_id}: {len(users_tags.get(str(chat_id)))}")
    else:
        print(f"{chat_id} has no subscriptions")
    return users_tags.get(str(chat_id))


def build_message(post):
    message_text = f"*{post.get('title')}*\n\n" + f"{post.get('description')}" + f"\n\nLink: {post.get('link')}"
    print(f"message {post.get('title')} is built")
    return message_text


def get_option_tag_from_message(text: str):
    print(f"got {text}")
    command_and_option = text.split(sep=' ')
    option_tags = [option.lower() for option in command_and_option[1:]]
    print(f'interpreted as {command_and_option[0]} {option_tags}')
    return option_tags


def parse_all_tags_txt(path='../DataTransfer/all_tags.txt'):
    """
    :param path: in case you need to parse another file
    :return: list of tags
    """

    with open(path, 'r') as file:
        tags = list()
        for line in file:
            tags.append(line.rstrip())
        return tags
