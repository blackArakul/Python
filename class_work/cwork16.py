# s = """
# Несколько
# строк
# """
# print(s)
#
# s1 = '''
# Несколько
# строк
# '''
# print(s1)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)  # Посмотреть документацию
# print(len.__doc__)

#
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print()
# print(zip.__doc__)

##############################
# print(ord("a"))  # Посмотреть код символа

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# string = "Test string for me"
#
# lst = [ord(i) for i in string]
# print(f'ASCII коды: {lst}')
#
# lst = [sum(lst) // len(lst)] + lst
# print(f"Средне арифметическое: {lst}")
#
# lst += [ord(num) for num in input("-> ")[:3] if ord(num) not in lst]
# # symbol3 = input("-> ")
# # for elem in symbol3[:3]:
# #     if ord(elem) not in lst:
# #         lst.append(ord(elem))
# print(lst)
#
# # count_last_num = 0
# # for num in lst[:-1]:
# #     if num == lst[-1]:
# #         count_last_num += 1
# # print(f'Количество последних элементов: {count_last_num}')
# print(f'Количество последних элементов: {lst.count(lst[-1]) - 1}')
#
# lst.sort(reverse=True)
# print(lst)


# ################################################
# print(chr(97))  # Выдает символ по его коду
# print(chr(11116))
# ###############################################


# a = 97
# b = 122
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")  # (a)97 > (A)65

#
# from random import randint
#
# shortest = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print(f"Ваш случайный пароль {random_password()}")


###############################################
# Методы строк

# s = "hello, WORLD! I am learning Python."

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.count(" "))
# print(s.count("l", 3))
# print(s.count("l", 3, 10))

# print(s.find("Python1"))  # возвращает индекс первого вхождения
# # Если элемента нет возвращает -1
# print(s.find("l", 4, 20))

# print(s.rfind("l"))  # ведет поиск с правой стороны
#
# print(s.index("l1"))  # Если значения нет ValueError
# print(s.rindex("l"))

# ########################################################
# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)


# print(s.startswith('hello'))
# print(s.index("I am"))
# print(s.endswith("on."))


# print(int("45"))

# ###################################################
# print("123".isdigit())  # Проверка, что внутри строки только цифры
# print('qqwwe1'.isalpha())  # Проверка, что внутри строки только буквы
#
#
# print('abc123'.isalnum())  # Внутри только буквы и цифры
#
# print('abc'.islower())  # Внутри только буквы lower регистре
# # не реагирует на цифры и спец символы
#
# print('ANF0123"&'.isupper())  # Внутри только буквы upper регистре
# # не реагирует на цифры и спец символы

##############################################
# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)
#############################################

# print("py".center(10))
# print(" py ".center(10, "'"))


###############
# Удаляет пробелы по умолчанию
# print('    py    '.lstrip())
# print('    py    '.rstrip())
# print('    py    '.strip())

# Удаляет перечень указанных символов
# print('https://www.pythons.org'.strip("/:pths.org"))
# print('https://www.pythons.org'.lstrip("/:pths").rstrip(".org"))


###############################
# Поиск и замена

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python"))


#################################
# Соединяет str.join(iterable(str))
# s = '-'
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))

##############################
#  Возвращает список строковых значений
# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org.ru'.split(".", 3))
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()
# b = list(map(int, a))
# print(b)


fio = input("Введите ФИО: ").split()

print(f'{fio[0]} {fio[1][0]}. {fio[2][0]}.')

