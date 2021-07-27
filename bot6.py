import os
import telebot 

bot = telebot.TeleBot('') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('Portada.pdf', 'rb')
    bot.send_document(id, document)

@bot.message_handler(commands=['gps'])
def documento(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.32302, -87.59408)

bot.polling()