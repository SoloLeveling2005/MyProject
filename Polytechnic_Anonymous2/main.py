import time
import os
import re
from random import randint
import telebot
from telebot import types  # кнопки Telegram
import datetime
import threading
import sqlite3 as sql

# Мои подключения
from connect import bot
from create_db import create_db
from check_new_request import application

print("Нажмите Ctrl+C если хотите завершить работу бота")


# with sql.connect("todo.db") as con:
#     cur = con.cursor()
#     cur.execute(f"""
#             CREATE TABLE IF NOT EXISTS users (
#                 id_user INTEGER NOT NULL,
#                 step INT NOT NULL,
#                 PRIMARY KEY(id_user)
#             )
#             """)
# # steps
# # 0 - по умолчанию
# # 1 - поиск анонимуса
# #
# #


def select_all_from_applications():
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      SELECT * FROM applications;
                      """)
        data_users = cur.fetchall()
    return data_users


def select_all_from_user_connection():
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      SELECT * FROM users_connection;
                      """)
        data_users = cur.fetchall()
    return data_users


def select_all_from_users():
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      SELECT * FROM users;
                      """)
        data_users = cur.fetchall()
    return data_users


@bot.message_handler(commands=['start'])
def start(message):
    id_user = message.chat.id
    users = select_all_from_users()
    for i in users:
        if i[id_user] == i[0]:
            main_menu(message)
            return
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                INSERT INTO users (id_user,step) VALUES({id_user},'default')
                """)
    main_menu(message)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "Доступные команды:")
    bot.send_message(message.chat.id,
                     "/main_menu " + "- перейти в главное меню")
    bot.send_message(message.chat.id,
                     "/find " + "- поиск анонимуса")
    bot.send_message(message.chat.id,
                     "/cancel " + "- отмена поиска")
    bot.send_message(message.chat.id,
                     "/disconnect " + "- отсоединиться от чата")
    bot.send_message(message.chat.id,
                     "Вам не обязательно их вводить, они будут доступны в виде кнопок ниже")


@bot.message_handler(commands=['main_menu'])
def command_main_menu(message):
    main_menu(message)


@bot.message_handler(commands=['find'])
def command_find_anonymous(message):
    find_anonymous(message)


@bot.message_handler(commands=['cancel'])
def command_cancel_find(message):
    id_user = message.chat.id
    bot.send_message(message.chat.id,
                     "Поиск отменен")
    main_menu(message)


@bot.message_handler(commands=['disconnect'])
def command_disconnect(message):
    main_menu(message)


def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('🔎Поиск анонимуса🔎')
    markup.add(find)
    bot.send_message(message.chat.id,
                     f"🏠Главное меню🏠",
                     parse_mode='HTML', reply_markup=markup)


def find_anonymous(message):
    id_user = message.chat.id
    user_connections = select_all_from_user_connection()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('Отмена поиска')
    markup.add(find)
    bot.send_message(message.chat.id,
                     f"🔎Начинаю поиск...",
                     parse_mode='HTML', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    while True:
        time_now = datetime.datetime.now()
        time_now = str(time_now).split(" ")
        time_now = str(time_now[1]).split(".")
        time_now = time_now[0]
        # print(time_now)

        try:
            bot.polling(none_stop=True)
            if time_now == "03:00:00" or time_now == "3:00:00":
                bot.send_message(1303257033,
                                 'Сообщение системы: Произошла перезагрузка программы')
                os.system('python main.py')
            time.sleep(1)

        except Exception as e:
            time.sleep(3)
            a = datetime.datetime.today()
            print(e)
            print(a)
            bot = telebot.TeleBot('5488566542:AAEGQsiDrnLjwFCQb4kmbn7EJYnZqoaIfxk')
            bot.send_message(1303257033,
                             'Сообщение системы: Произошла перезагрузка программы')
            os.system('python main.py')
