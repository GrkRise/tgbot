import telebot
import json

from telebot import types
from telebot.types import InlineKeyboardButton
import config

bot = telebot.TeleBot(config.ACCESS_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Приветствую тебя, хозяин. Ты написал мне /start")

@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.InlineKeyboardMarkup(True)
    keyboard.add(InlineKeyboardButton("start", callback_data="/start"),
                               InlineKeyboardButton("show web", callback_data="/show_web"))
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard)

@bot.message_handler(commands=['show_web'])
def show_web(message):
    markup = types.InlineKeyboardMarkup()
    btn_web = types.InlineKeyboardButton(text = 'web', url = 'https://core.telegram.org/bots/api')
    markup.add(btn_web)
    bot.send_message(message.chat.id, "Push", reply_markup= markup)

@bot.message_handler(commands=['switch'])
def switch_chat(message):
    markup = types.InlineKeyboardMarkup()
    btn_try = types.InlineKeyboardButton(text = 'try', switch_inline_query = 'Telegram')
    markup.add(btn_try)
    bot.send_message(message.chat.id, "Choose", reply_markup= markup)


@bot.message_handler(commands=['callback'])
def call_name(message):
    markup = types.InlineKeyboardMarkup()
    btn_a = types.InlineKeyboardButton(text = 'Rudolf', callback_data = 'Rudolf')
    btn_b = types.InlineKeyboardButton(text='Rudi', callback_data='Rudi')
    btn_c = types.InlineKeyboardButton(text='Rudik', callback_data='Rudik')
    markup.row(btn_a)
    markup.row(btn_b, btn_c)
    bot.send_message(message.chat.id, "Choose", reply_markup= markup)


@bot.callback_query_handler(func=lambda call : True)
def iq_callback(query):
    data = query.data
    if(data == "Rudolf"):
        bot.send_message(query.message.chat.id, "Yeah Rudolf")
    elif (data == "Rudik"):
        bot.send_message(query.message.chat.id, "Yes, Rudik")
    elif (data == "Rudi"):
        bot.send_message(query.message.chat.id, "No, no, no Rudi")
    bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Привет")
    elif message.text.lower() == "меня зовут люк":
        bot.send_message(message.chat.id, "Люк, я твой отец")
    elif message.text.lower() == "покажи свой стикер":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMJYVLazuQjZt9MkoaLy4YNFgeP7u4AAiMBAAKZj6UHhfUnEe8RmjQhBA')

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)

bot.polling()

