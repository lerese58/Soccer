import telebot
import requests

import Pusher.utils as pusher

from Puller.const import TOKEN

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
    posts = pusher.get_tagged_posts()
    message_text = pusher.build_message(posts[0])
    bot.send_message(message.chat.id, text=message_text, parse_mode="Markdown")


bot.polling(none_stop=True)
