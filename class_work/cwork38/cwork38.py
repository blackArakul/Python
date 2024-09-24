import sqlite3

# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
#
#     cur.execute("UPDATE cars SET price = :Price where model LIKE 'B%'", {'Price': 0})
# :Price именованный параметр

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list) - много однотипных запросов

# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)") - 1 SQL запрос
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()
# con.close()


#
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()  # Откатывает изменения к контрольной точки BEGIN;
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


#


# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row  # Это возможность работы обращения к элементам по ключам
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     # last_row_id = cur.lastrowid  # Возьмет у объекта id последней записи
#     # buy_car_id = 2
#     # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()  # Выводит все элементы
#     # rows = cur.fetchone()  # Выводит один элемент, смотря где находится курсор
#     # rows = cur.fetchmany(5)  # Выводит указанное кол-во элементов, смотря где находится курсор
#     # print(rows)
#
#     for res in cur:
#         # print(res[0], res[1])
#         print(res['model'], res['price'])


#


# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )""")
#
#     # img = read_ava("patreon_avatar_77")
#     # if img:
#     #     binary = sqlite3.Binary(img)  # Сохраняет как 16ричный код, удобный формат для модуля sqlite3
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)


# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():  # Служебный метод в который хранятся все запросы
#             f.write(sql)


# with sqlite3.connect("car_new.db") as con:
#     cur = con.cursor()
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)


#

#######################################################
# Шаблонизатор (Jinja2)

from jinja2 import Template


#
# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a }} лет. Меня зовут {{ n }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)


# per = {"name": "Игорь", "age": 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


#


# cities = [
#     {"id": 1, "city": "Москва"},
#     {"id": 2, "city": "Сочи"},
#     {"id": 3, "city": "Смоленск"},
#     {"id": 4, "city": "Ярославль"},
#     {"id": 5, "city": "Минск"}
# ]
#
# link = """
# <select name='cities'>
#     {% for c in cities -%}
#         {% if c.id > 3 -%}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == "Москва" %}
#             <option>{{ c['city'] }}</option>
#         {% else -%}
#             {{c['city']}}
#         {% endif -%}
#     {% endfor -%}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)
#

links = [
    {"href": "/index", "title": "Главная"},
    {"href": "/news", "title": "Новости"},
    {"href": "/about", "title": "О компании"},
    {"href": "/shop", "title": "Магазин"},
    {"href": "/contacts", "title": "Контакты"}
]

link = """
<ul>
    {% for l in links -%}
        {% if l.title != "Главная" -%}
            <li><a href="{{ l['href'] }}">{{ l['title'] }}</a></li>
        {% else -%}
            <li><a href="{{ l['href'] }}" class="active">{{ l['title'] }}</a></li>
        {% endif %}
    {% endfor %}
</ul>
"""

tm = Template(link)
msg = tm.render(links=links)

print(msg)









