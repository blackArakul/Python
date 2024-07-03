##################################################################################
# __repr__  и  __str__ Как работает


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# print(cat)  # __repr__
# print(cat[0])  # __str__


#


##########################################
# __len__ переопределяем метод

# class Point:
#     def __init__(self, *args):
#         self.coord = args
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))
#
# s = list((1, 2))
# print(len(s))


#
import math


#########################################################
# __slots__ ограничение, какие свойства могут быть в классе
# Экономие памяти
# Не наследуется


# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)  # Это отрабатывает setter
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# # p1.z = 30
# # print(p1.z)
# print(p1.length)
# p1.length = 20
# print(p1.length)


#


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2(1, 2)
# print("p1 =", pt1.__sizeof__())
# print("p2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


#


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = "z"
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# p1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 3
# print(pt3.z)


#


#################################################################
# Множественное наследование


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Rex")
#
# beast.bark()
# beast.sleep()
# beast.play()


#


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#         B.__init__(self)
#         C.__init__(self)
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)


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
# class Styles:
#     def __init__(self, color="red", width=1):
#         print(f"Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.mro())


#


###############################################################
# Миксины


# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init Mixin")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов ")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.save_sell_log()


#


#################################################################
# Перегрузка операторов

# 24 * 60 * 60 = 86400 - число секунд в одном дне


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
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         if self.sec == other.sec:
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)


# c1 = Clock(200)
# c2 = Clock(100)
# c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# c3 = c1 + c2 + c4
# print(c3.get_format_time())
# c1 += c2
# print(c1.get_format_time())

# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")


#


class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)


    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec == other.sec:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec < other.sec:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec <= other.sec:
            return True
        else:
            return False

    def __ge__(self, other):
        return not self.__le__(other)


c1 = Clock(600)
c2 = Clock(200)
print(f"c1: {c1.get_format_time()}")
print(f"c1 - c2: {(c1 - c2).get_format_time()}")
print(f"c1 * c2: {(c1 * c2).get_format_time()}")
print(f"c1 // c2: {(c1 // c2).get_format_time()}")
print(f"c1 % c2: {(c1 % c2).get_format_time()}")
print(f"c2 > c1 {c2 > c1}")
print(f"c2 >= c1 {c2 >= c1}")
print(f"c2 < c1 {c2 < c1}")
print(f"c2 <= c1 {c2 <= c1}")








