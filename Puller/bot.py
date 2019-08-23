import telebot
import requests

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


# TODO: /subscribe 'tag' <- user subscribes to 'tag'
# TODO: /tags <- sends user list of available tags sorted ascending

@bot.message_handler(commands=['subscribe'])
def subscription(message):
    # subscription logic happens *_*
    bot.send_message(message.chat.id, "Sorry, this command is not working yet")


@bot.message_handler(commands=['tags'])
def send_tags(message):
    # gets tags from database
    bot.send_message(message.chat.id, "Арсенал, Челси, Ливерпуль")


bot.polling(none_stop=True)
