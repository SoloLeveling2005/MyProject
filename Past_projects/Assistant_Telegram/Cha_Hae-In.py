import random
import time
import os
import re
from random import randint
import telebot
from telebot import types  # кнопки Telegram
import datetime
import threading
token = '5644245072:AAFlwhWoqzvwAYzIX2ZRr6FD5TS2AdKQhdc'
bot = telebot.TeleBot(token)

print("Нажмите Ctrl+C если хотите завершить работу бота")

id_chanel = "-1001673173066"
person = ""
# Сон Джинву, Ча Хэ Ин



# bot.send_message(id_chanel,'Сообщение системы: Произошла перезагрузка программы')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    mess = message.text
    mess = mess.lower()
    if "привет" in mess:
        time.sleep(random.randint(1, 5))
        bot.send_message(id_chanel,'Привет')









if __name__ == '__main__':
    while True:
        time_now = datetime.datetime.now()
        time_now = str(time_now).split(" ")
        time_now = str(time_now[1]).split(".")
        time_now = time_now[0]
        print(time_now)

        try:
            bot.polling(none_stop=True)
            if time_now == "03:00:00" or time_now == "3:00:00":
                bot.send_message(1303257033,
                                 'Сообщение системы: Произошла перезагрузка программы')
                os.system('python Cha_Hae-In.py')
            time.sleep(1)

        except Exception as e:
            time.sleep(3)
            a = datetime.datetime.today()
            print(e)
            print(a)
            bot = telebot.TeleBot('5441523880:AAEhN8ED9N3z0VwAXNQdktrWlYQRpGqIhMA')
            bot.send_message(1303257033,
                             'Сообщение системы: Произошла перезагрузка программы')
            os.system('python Cha_Hae-In.py')