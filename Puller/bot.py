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


bot.polling(none_stop=True)
