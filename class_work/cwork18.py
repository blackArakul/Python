#########################
# Регулярные выражения 2 часть
# Флаги

import re

# print(re.findall(r"\w+", "12 + й"))

# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))


# text = """
# one
# two
# """

# print(re. findall(r"one.\w+", text))
# print(re. findall(r"one.\w+", text, re.DOTALL))  # .(точка) учитывает \n

# print(re.findall(r"one$", text, re.MULTILINE))  # Многострочный текст

# print(re.findall("""
# [A-Za-z-0-9._-]+
# @
# [A-Za-z.-]+
# """, "test@mail.ru", re.VERBOSE))  # Позволяет включать в рег пробелы и переносы

##############################################
# Флаги в регулярном выражении

# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

###############################################
# +?, *?, ??
# {m,n}?, {,n}?, {m,}?
# Берет минимально допустимое значение


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

#####################################
# | - или, одно из перечисленных значений

# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[.\w]*"
# # reg = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w]*"
# reg = r"(int|float)\s*=\s*(\d[.\w]*)"
# print(re.findall(reg, s))
# print(re.search(reg, s))

##############################
# (?: ....) Означает что это группирующая скобка не является сохраняющей


########################################
# () Выводит тот элемент, который окружается
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# date = "01-12-2024"
# # reg = r"(\d{2})-(\d{2})-(\d{4})"
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, date))
# m = re.search(reg, date)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])
# print(re.search(reg, date).group())
# print(re.search(reg, date).group(1))  # Номер круглой скобки регулярного выражения
# print(re.search(reg, date).group(2))
# print(re.search(reg, date).group(3))


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
# count = 0
#
#
# def replace_find(var):
#     global count
#     count += 1
#     return f"<option value-'{count}'>{var.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))


# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))  # \число - обращение к скобке регулярного выражения

#
# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"https://\1", s))


###############################################################
# Рекурсия


# def elevator(num):
#     if num == 0:  # Базовый случай (условие выхода из рекурсии)
#         print("Вы в подвале")
#         return
#     print("=>", num)
#     elevator(num - 1)  # Должно быть изменение, что бы прийти к базовому случаю
#     print(num, end=" ")
#
#
# n1 = int(input("На каком этаже вы находитесь: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res


# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(num, base):
#     convert = "0123456789ABCDEF"
#     if num < base:
#         return convert[num]
#     else:
#         return to_str(num // base, base) + convert[num % base]
#
#
# print(to_str(254, 16))


def check_password(password):
    reg = r"[A-Za-z0-9\-@_]+"
    res = re.findall(reg, password)
    if 6 <= len(password) <= 18 and res[0] == password:
        print(f"Ваш пароль: {password} => верный")
    else:
        print("Пароль не верен!")


check_password("my-p@ss@w0rd")


















