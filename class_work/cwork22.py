##############################################################
#
#  ООП
#


# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.count += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.count -= 1
#
#         if Robot.count == 0:
#             print(f"{self.name} был последним")
#         else:
#             print(f"Работающих роботов осталось {Robot.count}")
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot("RD-D2")
# droid1.say_hi()
# print(f"Численность роботов {Robot.count}")
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f"Численность роботов {Robot.count}")
# droid3 = Robot("P-2PO")
# droid3.say_hi()
# print(f"Численность роботов {Robot.count}")
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу, давайте их выключим.")
# del droid1
# del droid2
# del droid3
# print(f"Численность роботов {Robot.count}")

#


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y  # _Point__y
#
#     def __check_value(a):  # _Point__check_value
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числами!")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должны быть числами!")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# # p1.set_coord(100, 200)
# # print(p1.get_coord())
# p1.set_x(50)
# print(p1.get_x())
# p1.set_y(30)
# print(p1.get_y())
# p1._Point__x = 111  # так лучше не делать
# print(p1.__dict__)
# print(p1._Point__x)


# import math
#
#
# class Rectangle:
#
#     __slots__ = ["__length", "__width", "x"]
#     ##########################################################################
#     # Определяет свойства с какими именами могут находиться в классе
#     # Не работает с __dict__
#
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(parameter):
#         if isinstance(parameter, int) or isinstance(parameter, float):
#             return True
#         return False
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def get_area(self):
#         return self.__length * self.__width
#
#     def get_perimeter(self):
#         return (self.__length + self.__width) * 2
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# rect = Rectangle(4, 12)
# rect.set_length(3)
# rect.set_width(9)
# print(f"Длина прямоугольника: {rect.get_length()}")
# print(f"Ширина прямоугольника: {rect.get_width()}")
# print(f"Площадь прямоугольника: {rect.get_area()}")
# print(f"Периметр прямоугольника: {rect.get_perimeter()}")
# print(f"Гипотенуза треугольна: {rect.get_hypotenuse()}")
# rect.get_draw()
# rect.x = 20
# print(rect.x)
# # print(rect.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("Сеттер")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


#


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(parameter):
#         if isinstance(parameter, int) or isinstance(parameter, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 50
# print(p1.x)
# del p1.x
# print(p1.__dict__)


#


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются числами!")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(f"{weight.kg} кг => {weight.to_pound()} фунтов")
# weight.kg = 41
# print(f"{weight.kg} кг => {weight.to_pound()} фунтов")
# weight.kg = "два"


#


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
# p5 = Point()
#
# print(Point.get_count())


class Person:

    def __init__(self, name, old):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Имя введено не корректно")
        if isinstance(old, int):
            self.__old = old
        else:
            print("Возраст введен не корректно")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Имя введено не корректно")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if isinstance(new_old, int):
            self.__old = new_old
        else:
            print("Возраст введен не корректно")

    @old.deleter
    def old(self):
        del self.__old


personality = Person("Irina", 26)
print(personality.__dict__)
personality.name = "Igor"
print(personality.name)
personality.old = 31
print(personality.old)
del personality.name
print(personality.__dict__)







