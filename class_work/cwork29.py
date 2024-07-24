#################################################
# Метаклассы


# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
# def get_length(self):
#     return len(self)


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())  # [5, 7] 2


#


#######################################################
#  Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import *

# from geometry import rect, sq, trian
#
#
# def main():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     main()
#


#


# from car.electrocar import ElectroCar
#
#
# if __name__ == '__main__':
#     e_car = ElectroCar("Tesla", "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()


#
from employee.comission_employee import CommissionEmployee
from employee.salary_employee import SalaryEmployee
from employee.hourly_employee import HourlyEmployee
from employee.payroll_system import PayrollSystem


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commission_employee
])


#


#################################################
# Упаковка и распаковка данных
# # Сериализация
# # Десериализация


# marshal (*.pyc)
# pickle (работает только в пайтон)
# json (из почти любого языка)

import pickle

# file_name = "../basket.txt"
# shop_list = {
#     "фрукты":  ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)


# class Text:
#     num = 35
#     string = "Hello"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}"
#
#
# obj = Text()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# obj2 = pickle.loads(my_obj)
# print(obj2)








