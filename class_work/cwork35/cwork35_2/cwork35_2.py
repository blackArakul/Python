# SQLite

import sqlite3

# 1 - вариант

# con = sqlite3.connect("profile.db")
# # Соединение с базой данных
# # Если не существует базы с таким именем, то оне ее создаст
#
# cur = con.cursor()
# # Обращения к базе данных
#
# cur.execute("""""")
# con.close()


# 2 - вариант


# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB)""")
#     cur.execute("DROP TABLE users")


#


# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     DROP TABLE person_table
#     """)

# Удаление столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address
    # """)

# Смена имени столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address
    # """)

# Добавление столбца в таблицу
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT;
    # """)

# Смена имени таблицы

    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

# Создание таблицы

    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT "+79099000000",
    # age INTEGER CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")


with sqlite3.connect("db_4.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5 
    """)





















