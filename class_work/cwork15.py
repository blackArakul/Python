#  Декораторы

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"


# print(hello())


# def decorator(func):
#     count = 0
#
#     def fn_count():
#         nonlocal count
#         count += 1
#         func()
#         print("Вызовов функций", count)
#
#     return fn_count
#
#
# @decorator
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(*args):
#         print("Данные:", *args)
#         fn(*args)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Эстебан", "Мальдини")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# func("John", "Piter", "Michael", study="JavaScript")
# func("Bred", "Tomas", "Liza")

# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
#
#
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor_args("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(num):
#     def func(fn):
#         def mult_num(ch):
#             print("Результат:", end=" ")
#             return num * fn(ch)
#
#         return mult_num
#
#     return func
#
#
# @multiply(3)
# def return_num(number):
#     return number
#
#
# print(return_num(5))


# Строки

# print(int("19"))
# print(int("19.5"))
# print(int(19.5))


# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))


# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0x12)


# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * 2)
# print("y" in e)
# print(e[0])
# print(e[1:3])


# s = "Python"
# # s[3] = "t"  # ошибка
# s = s[:3] + "t" + s[4:]
# print(s)


# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
#
# str2 = change_char_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)


# Префиксы строк

# print("Привет")
# print(u"Привет")  # u - стандарт unicode

# print("C:\\folder\\fi\nle.txt\\")
# print(r"C:\folder\fi\nle.txt\\"[:-1])  # r - подавляет экранирование, не работают спецсимволы
# print(r"C:\folder\fi\nle.txt" + "\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# ch = 5.131231312
#
# print(f"Число {round(ch, 2)}")
# print(f"Число {ch:.3f}")


# x = 100
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * x / 2}")


# num = 74
# print(f"{{{num}}}")


# dir_name = "my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")


def decorator(func):
    def arif(*args):
        print(f"Сумма чисел {args}: {func(*args)}\nСредне арифметическое {args}:", end=" ")

        return func(*args) / len(args)

    return arif


@decorator
def summa(*args):
    return sum(args)


print(summa(5, 5, 5, 5, 5, 5))
