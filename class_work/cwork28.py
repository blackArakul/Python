#############################################################
#
#  Функторы - это объекты класса, которые можно выполнять как функции


# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()


#


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1)
# print(s1(" :?.Hello World! "))  # Hello World


#

#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     # def __call__(self, *args, **kwargs):
#     #     if not isinstance(args[0], str):
#     #         raise ValueError("Аргумент должен быть строкой")
#     #     return args[0].strip(self.__chars)
#
#     def __call__(self, string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s2 = StripChars("?:!.; ")
# print(s2(" :?.Hello World! "))


#


################################################################################
# Класс как декоратор


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.fn()
#         print("После вызовом функции")
#
#
# @MyDecorator
# def func():
#     print("Hello world")
#
#
# func()


#


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         # print("Перед вызовом функции")
#         # self.fn(x, y)
#         # print("После вызовом функции")
#         return f"Перед вызовом функции\n{self.fn(x, y)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


#


# class Power:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         return f"Результат: {self.func(a, b) ** 2}"
#
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print(func(2, 3))


#


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))
# print(func1(2, c=5, b=2))


#


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             return f"Перед вызовом функции\n{self.arg} {args[0]} * {args[1]} {fn(*args, **kwargs)}\nПосле вызова функции"
#         return wrap
#
#
# @MyDecorator("Произведение: ")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


#

# class Power:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def __call__(self, fn):
#         def raise_degree(*args, **kwargs):
#             return f"Результат: {fn(*args, **kwargs) ** self.degree}"
#
#         return raise_degree
#
#
# @Power(3)
# def test_func(a, b):
#     return a * b
#
#
# print(test_func(2, 2))


#


############################################################
# Декорирование методов класса

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Некрасов")
#
# p1.info()


#
##############################################################################
# Декорирование класса

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(5))
# print(obj.doubler(5))


#


#################################################################################
# Дескриптор

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__name
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())


########################################################################

# Дескриптор (__get__, __set__, __set_name__, __delete__)


# class ValidString:
#     def __set_name__(self, owner, name):
#         # print(owner)
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# p.surname = "Иванов"
# print(p.name)
# print(p.surname)


#


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name  # getattr и setattr без добавки выдает ошибку RecursionError
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]  # Более безопасно
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Значение {self.name} должно быть положительное")
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order("apple", 5, 10)
# apple_order.quantity = 15
# print(apple_order.price)
# print(apple_order.total())
# print(apple_order.__dict__)


class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {self.name} должно быть целочисленное")
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3D(2, 5, 6)
print(p1.__dict__)




