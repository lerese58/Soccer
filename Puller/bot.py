import telebot
import requests

import Pusher.utils as pusher
import Puller.utils as puller

from Puller.settings import TOKEN, LATEST_POSTS_PATH, USERS_PATH

session = requests.Session()
session.verify = False

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_hi(message):
    bot.send_message(message.chat.id,
                     "Greetings, traveler!\n" +
                     "To get help press /help.")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Help")


@bot.message_handler(commands=['get'])
def send_post(message):
    tags = puller.get_option_tag_from_message(message.text) or puller.get_tags_for(message.chat.id)
    posts_for_message = puller.get_posts_for(tags)
    for p in posts_for_message:
        message_text = puller.build_message(p)
        bot.send_message(message.chat.id, text=message_text, parse_mode="Markdown")


@bot.message_handler(commands=['subscribe', 'sub'])
def subscribe(message):
    chat_id = message.chat.id
    tags = puller.get_option_tag_from_message(message.text)
    users_tags: dict = puller.decode_json(USERS_PATH)
    if users_tags.get(str(chat_id)) is None:
        users_tags[str(chat_id)] = []
    for tag in tags:
        if tag not in users_tags.get(str(chat_id)):
            users_tags.get(str(chat_id)).append(tag)
            print(f"{chat_id} subscribes to {tag}")
            bot.send_message(chat_id, text=f"Successfully subscribed to '{tag}'")
        else:
            print(f"{chat_id} tries to subscribe to {tag} one more time")
            bot.send_message(chat_id, text=f"You've already subscribed to '{tag}'")
    pusher.make_json(users_tags, USERS_PATH)


@bot.message_handler(commands=['unsubscribe', 'unsub'])
def unsubscribe(message):
    chat_id = message.chat.id
    tags = puller.get_option_tag_from_message(message.text)
    if not tags:
        bot.send_message(chat_id, "Command 'unsubscribe' should contains at least one tag")
        print(f"'/unsubscribe' w/o tags from {chat_id}")
    users_tags: dict = puller.decode_json(USERS_PATH)
    for tag in tags:
        if tag in users_tags.get(str(chat_id)):
            users_tags.get(str(chat_id)).remove(tag)
            print(f"'{tag}' removed from tags for {chat_id}")
            bot.send_message(chat_id, f"'{tag}' successfully removed from your tags")
        else:
            print(f"'{tag}' not found in tags for {chat_id}")
            bot.send_message(chat_id, f"'{tag}' not found")
    pusher.make_json(users_tags, USERS_PATH)


@bot.message_handler(commands=['mytags', 'my'])
def send_my_tags(message):
    chat_id = message.chat.id
    tag_list = puller.get_tags_for(chat_id)
    message_text = str(tag_list)
    bot.send_message(chat_id, text=message_text)


@bot.message_handler(commands=['alltags', 'all'])
def send_all_tags(message):
    tags = puller.parse_all_tags_txt()
    message_text = str(tags)
    bot.send_message(message.chat.id, text=message_text)


bot.polling(none_stop=True)
