######################################################################
###########
# ООП
import re


##############################################################
# @staticmethod


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))


#


# class CountMax:
#     @staticmethod
#     def max_num(*args):
#         return max(args)
#
#     @staticmethod
#     def min_num(*args):
#         return min(args)
#
#     @staticmethod
#     def arif(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def fact(num):
#         res = 1
#         for i in range(1, num+1):
#             res *= i
#         return res
#
#
# print(CountMax.max_num(3, 5, 7, 9))
# print(CountMax.min_num(3, 5, 7, 9))
# print(CountMax.arif(3, 5, 7, 9))
# print(CountMax.fact(5))


#


################################################################
# Методы класса

#
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     "25.10.2024",
#     "23-10-2023",
#     "01.01.2021",
#     "12.31.2020"
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         print(date.string_to_db())
#     else:
#         print("Неправильный формат строки с датой")
#
# # date2 = Date(23, 10, 2023)
# # date2 = Date.from_string("23-10-2023")
# # print(date2.string_to_db())
# #
# # date3 = Date.from_string("25.10.2024")
# # print(date3.string_to_db())
#
# # day, month, year = map(int, string_date.split("."))
# # date = Date(day, month, year)


#


# class Account:
#     rub_usd = 0.011
#     rub_eur = 0.010
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, acc_num, percent, sum_of_rub):
#         self.surname = surname
#         self.acc_num = acc_num
#         self.percent = percent
#         self.sum_of_rub = sum_of_rub
#         print(f"Счет #{self.acc_num} принадлежащий {self.surname} был открыт")
#         print("*" * 40)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.acc_num} принадлежащий {self.surname} был закрыт")
#
#     @classmethod
#     def set_usd_course(cls, new_course):
#         cls.rub_usd = new_course
#
#     @classmethod
#     def set_eur_course(cls, new_course):
#         cls.rub_eur = new_course
#
#     @staticmethod
#     def convert(value, course):
#         return value * course
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.sum_of_rub, Account.rub_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.sum_of_rub, Account.rub_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def edit_owner(self, new_surname):
#         self.surname = new_surname
#
#     def add_percents(self):
#         self.sum_of_rub += self.sum_of_rub * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def draw_money(self, draw):
#         if draw > self.sum_of_rub:
#             print(f"К сожалению у вас нет {draw} {Account.suffix}")
#         else:
#             self.sum_of_rub -= draw
#             print(f"{draw} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, add_money):
#         self.sum_of_rub += add_money
#         print(f"{add_money} {Account.suffix} было успешно добавлена")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.sum_of_rub} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.acc_num}\nВладелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_course(2)
# acc.convert_to_usd()
# Account.set_eur_course(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.draw_money(3000)
# print()
#
# acc.draw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.draw_money(3000)
# print()


#


# class UserDate:
#
#     def __init__(self, fio, old, password, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_password(password)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = password
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ["Волков", "Игорь", "Николаевич"]
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # Вол-ковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(weight):
#         if not isinstance(weight, float) or weight < 30:
#             raise TypeError("Вес должен быть вещественным числом от 30кг и выше")
#
#     @staticmethod
#     def verify_password(passw):
#         if not isinstance(passw, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = passw.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# person1 = UserDate("Волков-Петров Игорь Николаевич", 26, "1234 567890", 30.3)


#

import math


class CalcArea:
    __count = 0

    def __del__(self):
        print(f"Количество подсчетов площади: {CalcArea.__count}")

    @staticmethod
    def check_value(parameter):
        if not isinstance(parameter, (int, float)):
            raise TypeError("Стороны должны быть числом")

    @staticmethod
    def get_area_triangle_ger(a, b, c):
        if CalcArea.check_value(a) and CalcArea.check_value(b) and CalcArea.check_value(c):
            return None
        else:
            p = (a + b + c) / 2
            CalcArea.__count += 1
            return round(math.sqrt(p * (p-a)*(p-b)*(p-c)), 2)

    @staticmethod
    def get_area_triangle(a, b):
        if CalcArea.check_value(a) and CalcArea.check_value(b):
            return None
        else:
            CalcArea.__count += 1
            return 0.5 * a * b

    @staticmethod
    def box_area(side):
        if CalcArea.check_value(side):
            return None
        else:
            CalcArea.__count += 1
            return side ** 2

    @staticmethod
    def rectangle_area(a, b):
        if CalcArea.check_value(a) and CalcArea.check_value(b):
            return None
        else:
            CalcArea.__count += 1
            return a * b


calc_area1 = CalcArea()
print(f"Площадь треугольника по формуле Герона (3, 5, 7):  {calc_area1.get_area_triangle_ger(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту(6,7): {calc_area1.get_area_triangle(6, 7)}")
print(f"Площадь квадрата (7): {calc_area1.box_area(7)}")
print(f"Площадь прямоугольника (2,6): {calc_area1.rectangle_area(2, 6)}")

