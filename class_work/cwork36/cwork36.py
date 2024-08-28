#####################################################
# SQLite
import sqlite3


with sqlite3.connect("db_4.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5 
    """)
    # res = cur.fetchall()
    # Возвращает список кортежей, все записи

    # res = cur.fetchone()
    # print(res)
    # # Возвращает первую запись кортежем
    # res = cur.fetchone()

    # res = cur.fetchmany()
    # Возвращает список из одного кортежа
    # res = cur.fetchmany(2)
    # Возвращает список кортежей по аргументу size

    for res in cur:
        print(res)







