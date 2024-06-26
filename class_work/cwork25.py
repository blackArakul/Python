###########################################################
# ООП


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
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть реализован метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(10, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(30, 30)))
#
#
# for f in figs:
#     f.draw()

##############################################################################
# Абстрактные методы


# Абстрактный класс

# from math import pi
# from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()


#


# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод clac_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())


#


# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 40)
# for elem in d:
#     elem.print_value()
#     elem.show()
#
# print("*" * 40)
# for elem in e:
#     elem.print_value()
#     elem.show()


#


###################################################################
# Интерфейсы


# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#
#     def display1(self):
#         print("Child class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild class")
#
#
# ch = GrandChild()
# ch.display1()
# ch.display2()


#


####################################################################
# Вложенные классы


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("outer_method")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный метод", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter("внешний")
# print(out.name)
# inner = out.MyInner("внутренний", out)
# print(inner.inner_name)
# inner.inner_method()


#


# class DarkGreen:
#     def __init__(self):
#         self.name = "Dark Green"
#
#     def display(self):
#         print(f"Name {self.name}")
#
#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#         self.dg = DarkGreen()
#
#     def show(self):
#         print(f"Name {self.name}")
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print(f"Name {self.name}")
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# g2 = outer.dg
# g2.display()
# print(g2.name)


#
# class PC:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = PC()
# # my_os = comp.os
# # my_cpu = comp.cpu
# my_os = PC().OS()
# my_cpu = PC().CPU()
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


#


class Student:
    def __init__(self, name):
        self.name = name
        # self.pc = self.PC()

    def print_info(self):
        print(f'{self.name} => {self.PC().system()}')

    class PC:
        @staticmethod
        def system():
            return "HP, i7, 16"


students = [Student("Roman"), Student("Vladimir")]

for elem in students:
    elem.print_info()




















