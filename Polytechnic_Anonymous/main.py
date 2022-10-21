import time
import os
import re
from random import randint
from connect import bot
import telebot
from telebot import types  # кнопки Telegram
import datetime
import threading
import sqlite3 as sql

print("Нажмите Ctrl+C если хотите завершить работу бота")

found = 0

with sql.connect("todo.db") as con:
    cur = con.cursor()
    cur.execute(f"""
            CREATE TABLE IF NOT EXISTS users (
                ID INTEGER NOT NULL,
                id_one INT NOT NULL,
                id_two INT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT)
            )
            """)
with sql.connect("todo.db") as con:
    cur = con.cursor()
    cur.execute(f"""
            CREATE TABLE IF NOT EXISTS applications (
                ID INTEGER NOT NULL,
                id_user INT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT)
            )
            """)


def applications():
    while True:
        with sql.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(f"""
                          SELECT * FROM applications;
                          """)
            data_users = cur.fetchall()
            if len(data_users) > 1:
                one_id = data_users[0][1]
                two_id = data_users[1][1]
                with sql.connect("todo.db") as con:
                    cur = con.cursor()
                    cur.execute(f"""
                            INSERT INTO users (id_one,id_two) VALUES('{one_id}','{two_id}')
                            """)
                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {data_users[0][1]};
                                  """)

                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {data_users[0][1]};
                                  """)
        time.sleep(1)

applications_thread = threading.Thread(target=applications)
applications_thread.daemon = True
applications_thread.start()


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    print(user_id)
    start_chat(message)


def start_chat(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('Поиск анонимуса')
    markup.add(find)
    bot.send_message(message.chat.id,
                     f"Добро пожаловать",
                     parse_mode='HTML', reply_markup=markup)


def main_menu(message):
    global found
    found = 0
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      SELECT * FROM applications;
                      """)
        data_users = cur.fetchall()
        if len(data_users) > 1:
            try:
                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {data_users[0][1]};
                                  """)
            except:
                pass
            try:
                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {data_users[0][1]};
                                  """)
            except:
                pass

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('Поиск анонимуса')
    markup.add(find)
    bot.send_message(message.chat.id,
                     f"Отменил",
                     parse_mode='HTML', reply_markup=markup)
def close(message):
    global found
    found = 0
    id_user = message.chat.id
    id_two = None
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      SELECT * FROM users;
                      """)
        data_users = cur.fetchall()
    for i in data_users:
        print(id_user)
        print(i)
        if i[1] == id_user:
            id_two = i[2]
        elif i[2] == id_user:
            id_two = i[1]
    with sql.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(f"""
                      DELETE FROM users WHERE id_one = {id_user};
                      """)



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('Поиск анонимуса')
    markup.add(find)
    bot.send_message(message.chat.id,
                     f"Вы вышли из чата",
                     parse_mode='HTML', reply_markup=markup)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    find = types.KeyboardButton('Поиск анонимуса')
    markup.add(find)
    bot.send_message(id_two,
                     f"Анонимус вышел из чата",
                     parse_mode='HTML', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global found
    user_id = message.from_user.id
    if message.text == 'Поиск анонимуса':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        cancel_find = types.KeyboardButton('Отмена поиска')
        markup.add(cancel_find)

        bot.send_message(message.chat.id,
                         f"Начинаю поиск...",
                         parse_mode='HTML', reply_markup=markup)

        with sql.connect("todo.db") as con:
            cur = con.cursor()
            cur.execute(f"""
                    INSERT INTO applications (id_user) VALUES('{user_id}')
                    """)
        print(user_id)
        def hm():
            global found
            with sql.connect('todo.db') as con:
                cur = con.cursor()
                cur.execute(f"""
                              SELECT * FROM users;
                              """)
                data_users = cur.fetchall()

            for i in data_users:
                print("цикл работает")
                if i[1] == user_id:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    cancel_find = types.KeyboardButton('Отсоединиться')
                    markup.add(cancel_find)
                    bot.send_message(user_id,
                                     f"Нашел",
                                     parse_mode='HTML', reply_markup=markup)
                    bot.send_message(i[2],
                                     f"Нашел",
                                     parse_mode='HTML', reply_markup=markup)
                    found = 1
                    break
                else:
                    print("No")


        while True:
            time.sleep(2)

            if found == 1:
                print("Нашел")
                break
            else:
                hm_thread = threading.Thread(target=hm)
                hm_thread.daemon = True
                hm_thread.start()

    elif message.text == 'Отсоединиться':
        close(message)
    elif message.text == 'Отмена поиска':
        main_menu(message)
    else:
        print(found)
        if found == 1:
            print(message.text)


            with sql.connect('todo.db') as con:
                cur = con.cursor()
                cur.execute(f"""
                              SELECT * FROM users;
                              """)
                data_users = cur.fetchall()

                for i in data_users:
                    if i[1] == user_id:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        cancel_find = types.KeyboardButton('Отсоединиться')
                        markup.add(cancel_find)
                        bot.send_message(i[2],
                                         f"""
                                         &#128128;{message.text}
                                        """,
                                         parse_mode='HTML', reply_markup=markup)
                        break
                    elif i[2] == user_id:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        cancel_find = types.KeyboardButton('Отсоединиться')
                        markup.add(cancel_find)
                        bot.send_message(i[1],
                                         f"""
                                         &#128128;{message.text}
                                        """,
                                         parse_mode="HTML", reply_markup=markup)
                        break
        # with sql.connect('todo.db') as con:
        #     cur = con.cursor()
        #     cur.execute(f"""
        #                   DELETE FROM users WHERE my_id = {user_id};
        #                   """)
        #
        # with sql.connect("users.db") as con:
        #     cur = con.cursor()
        #     cur.execute(f"""
        #             INSERT INTO users (my_id,companion_id) VALUES('{user_id}','{new_password}')
        #             """)

        # with sql.connect('users') as con:
        #     cur = con.cursor()
        #     cur.execute(f"""
        #                   SELECT companion_id FROM users WHERE my_id = 40;
        #                   """)
        #     data_users = cur.fetchall()



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
