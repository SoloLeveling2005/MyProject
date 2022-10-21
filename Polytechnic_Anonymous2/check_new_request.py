import time
import sqlite3 as sql
import threading


def application_threading():
    applications_thread = threading.Thread(target=application)
    applications_thread.daemon = True
    applications_thread.start()


def application():
    while True:
        with sql.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute(f"""
                          SELECT * FROM applications;
                          """)
            application_users = cur.fetchall()
            if len(application_users) > 1:
                one_id = application_users[0][0]
                two_id = application_users[1][0]
                with sql.connect("todo.db") as con:
                    cur = con.cursor()
                    cur.execute(f"""
                            INSERT INTO users_connection (one,two) VALUES('{one_id}','{two_id}')
                            """)
                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {one_id};
                                  """)

                with sql.connect('todo.db') as con:
                    cur = con.cursor()
                    cur.execute(f"""
                                  DELETE FROM applications WHERE id_user = {one_id};
                                  """)
        time.sleep(2)