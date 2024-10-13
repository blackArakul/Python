import sqlite3
import math
import time


class SFData:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except Exception as e:
            print(e)
        return []

    def add_course(self, name, price, url, info):
        try:
            self.__cur.execute("SELECT COUNT() as 'count' FROM courses WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким URL уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO courses VALUES (NULL, ?, ?, ?, ?, ?)", (name, price, url, info, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавление статьи в базу данных" + str(e))
            return False
        return True

    def get_course(self, alias):
        try:
            self.__cur.execute(f"SELECT name, price, info FROM courses WHERE url='{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка добавление статьи в базу данных" + str(e))
        return False, False, False

    def get_course_announce(self):
        try:
            self.__cur.execute("SELECT name, price, url, info FROM courses ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка добавление статьи в базу данных" + str(e))
        return []


