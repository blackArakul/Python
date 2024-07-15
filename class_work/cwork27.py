#####################################################################
# Перегрузка квадратных скобок


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Указанного индекса не существует")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


#


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 11
# c1["min"] = 24
# c1["sec"] = 52
# print(c1["hour"], c1["min"], c1["sec"])


#


# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is a good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is a good girl!!!"
#         else:
#             return f"{self.name} is a good kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# # print(cat2)
# print(cat3)
# print(cat1 + cat2)


#


############################################################
# Полиморфизм


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)

# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


#


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# for animal in [cat1, dog1]:
#     print(f"{animal.info()}\n{animal.make_sound()}")


#


# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(self.speciality, self.group, self.rating, end="")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, diploma):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.diploma = diploma
#
#     def info(self):
#         super().info()
#         print(f"{self.diploma}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(self.speciality, self.rating, end=" ")
#
#
# group1 = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_001", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Данькшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python", 5),
#     Teacher("Башикров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group1:
#     i.info()


#


from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimetr(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def print_figure(self):
        pass


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_perimetr(self):
        return f"Периметр: {4 * self.side}"

    def get_area(self):
        return f"Площадь: {self.side ** 2}"

    def print_figure(self):
        for i in range(self.side):
            if i == 0 or i == self.side - 1:
                print("+" * self.side)
            else:
                print("+" + " " * (self.side - 2) + "+")

    def print_info(self):
        print(f"===Квадрат===\nСторона: {self.side}\nЦвет: {self.color}\n{self.get_area()}\n{self.get_perimetr()}")
        self.print_figure()


class Rectangle(Shape):
    def __init__(self, color, h, w):
        super().__init__(color)
        self.w = w
        self.h = h

    def get_perimetr(self):
        return f"Периметр: {2 * self.w + self.h}"

    def get_area(self):
        return f"Площадь: {self.h * self.w}"

    def print_figure(self):
        for i in range(self.h):
            if i == 0 or i == self.h - 1:
                print("+" * self.w)
            else:
                print("+" + " " * (self.w - 2) + "+")

    def print_info(self):
        print(f"===Прямоугольник===\nДлина: {self.h}\nШирина: {self.w}\nЦвет: {self.color}\n{self.get_area()}\n{self.get_perimetr()}")
        self.print_figure()


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimetr(self):
        return f"Периметр: {self.side1 + self.side2 + self.side3}"

    def get_area(self):
        s = (self.side1 + self.side2 + self.side3) // 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def print_figure(self):
        for i in range(self.side2):
            spaces = " " * (self.side2 - i - 1)
            stars = "+" * (2 * i + 1)
            print(spaces + stars)

    def print_info(self):
        print(f"===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\nЦвет: {self.color}\n{self.get_area()}\n{self.get_perimetr()}")
        self.print_figure()


s1 = Square("Red", 5)
s1.print_info()

r1 = Rectangle("green", 3, 10)
r1.print_info()

t1 = Triangle("blue", 11, 6, 6)
t1.print_info()




























