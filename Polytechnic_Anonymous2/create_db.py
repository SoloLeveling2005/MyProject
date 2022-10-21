import sqlite3 as sql




def create_db():
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                CREATE TABLE IF NOT EXISTS users_connection (
                    ID INTEGER NOT NULL,
                    one INT NOT NULL,
                    two INT NOT NULL,

                    PRIMARY KEY(ID AUTOINCREMENT)
                )
                """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                CREATE TABLE IF NOT EXISTS applications (
                    id_user INTEGER NOT NULL

                )
                """)
    with sql.connect("todo.db") as con:
        cur = con.cursor()
        cur.execute(f"""
                CREATE TABLE IF NOT EXISTS users (
                    id_user INTEGER NOT NULL,
                    step VARCHAR(30) NOT NULL

                )
                """)