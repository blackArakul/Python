########################################################################
# ООП

# import re


# class UserDate:
#
#     def __init__(self, fio, old, password, weight):
#         self.fio = fio
#         self.old = old
#         self.password = password
#         self.weight = weight
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
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, password):
#         self.verify_password(password)
#         self.__password = password
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# person1 = UserDate("Волков-Петров Игорь Николаевич", 26, "1234 567890", 30.3)
#
# # person1.fio = "Соболев Игорь Николаевич"
# print(person1.__dict__)


#


##############################################################################
# Наследование

#
# class Point:  # (object)
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # Должен вернуть строковое представление
#         return f"({self.__x}, {self.__y})"
#
#
# ###############################################################################################
# # print(issubclass(Point, object))  # Наследуется ли класс от второго класса(второй параметра)
# # Возвращает Boolean значение
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Переопределенный инициализатор class Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор class Line")
#
#     def draw_line(self) -> None:  # Какой тип данных возвращается
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #     def draw_rect(self):  # Какой тип данных возвращается
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
#
# # rect = Rect(Point(30, 40), Point(70, 70))
# # rect.draw_rect()
#
# # print(issubclass(Line, Prop))
# # print(issubclass(Line, Rect))
# # print(Point.__dict__)
# # print(Line.__dict__)
# # print(Prop.__dict__)


#


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом!")
#
#     @property
#     def height(self):
#         return self.__width
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__width = h
#         else:
#             raise ValueError("Высота должна быть положительным числом!")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
#
# # rect.width = -50
# # print(rect.width)
#
# print(rect.area())


#


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, bg_color):
#         super().__init__(width, height)
#         self.bg_color = bg_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.bg_color}")
#
#
# class RectBorder(Rect):
#     # 1px solid red
#     def __init__(self, width, height, border_width, border_type, border_color):
#         super().__init__(width, height)
#         self.border_width = border_width
#         self.border_type = border_type
#         self.border_color = border_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Ширина рамки: {self.border_width}\nТип рамки: {self.border_type}\nЦвет рамки: {self.border_color}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
#
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()


#

###############################################################
# Наследование от существующих классов


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


#


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self) -> None:  # Какой тип данных возвращается
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# ###############################################################################
# # Перегрузка методов
# # Возможность выбрать принимаемый аргументы, который требуется изменить
#     def set_coord(self, sp: Point = None, ep: Point = None):
#         if ep is None:
#             self._sp = sp
#         elif sp is None:
#             self._ep = ep
#         else:
#             self._sp = sp
#             self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(12, 18), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()
# line.set_coord(ep=Point(500, 700))
# line.draw_line()


#


import math


class Pair:
    def __init__(self, num_a, num_b):
        if num_a > 0 and num_b > 0:
            self._num_a = num_a
            self._num_b = num_b
        else:
            raise ValueError("Число должно быть положительным!")

    def set_a(self, new_num_a):
        if new_num_a > 0:
            self._num_a = new_num_a
        else:
            raise ValueError("Число должно быть положительным!")

    def set_b(self, new_num_b):
        if new_num_b > 0:
            self._num_b = new_num_b
        else:
            raise ValueError("Число должно быть положительным!")

    def get_sum(self):
        return self._num_a + self._num_b

    def get_multiply(self):
        return self._num_a * self._num_b


class RightTriangle(Pair):
    def __init__(self, num_a, num_b):
        super().__init__(num_a, num_b)

    def get_hypotenuse(self):
        return round(math.sqrt(self._num_a**2 + self._num_b**2), 2)

    def get_area(self):
        return 0.5 * self._num_a * self._num_b

    def get_info(self):
        print(f"Прямоугольный треугольник ABC ({self._num_a}, {self._num_b}, {self.get_hypotenuse()})")


triangle = RightTriangle(5, 8)
print(f"Гипотенуза ABC: {triangle.get_hypotenuse()}")
triangle.get_info()
print(f"Площадь ABC: {triangle.get_area()}")
print()
print(f"Сумма: {triangle.get_sum()}")
print(f"Произведение: {triangle.get_multiply()}")
print()
triangle.set_b(20)
triangle.set_a(10)
print(f"Гипотенуза ABC: {triangle.get_hypotenuse()}")
print(f"Сумма: {triangle.get_sum()}")
print(f"Произведение: {triangle.get_multiply()}")
print(f"Площадь ABC: {triangle.get_area()}")






