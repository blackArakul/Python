# lst = [5, 6, 8, 9, 7]
# if len(lst) == 0:
#     print("Список пустой")

# if not lst:  # Не явное преобразование типов данных
#     print("Список пустой")


# print(5 not in lst)

# import random

# array1 = [random.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# array2 = [random.randint(0, 10) for i in range(int(input("Введите размер второго списка: ")))]
# print("Первый список:", array1)
# print("Второй список:", array2)
#
# array3 = array1 + array2
# print("Третий список:", array3)
# array3.clear()
#
# for i in range(len(array1)):
#     if array1[i] not in array3:
#         array3.append(array1[i])
# for i in range(len(array2)):
#     if array2[i] not in array3:
#         array3.append(array2[i])
# print("Элементы обоих списков без повторений", array3)
# array3.clear()
#
#
# for elem in array1:
#     if elem in array2 and elem not in array3:
#         array3.append(elem)
#
# print("Общие элементы двух списков", array3)
# array3.clear()
#
# array3 = [min(array1), min(array2), max(array1), max(array2)]
# print(array3)


# Вложенные списки (матрица)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(m[1][2])
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# # print(matrix)


# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
#
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# w, h = 3, 4
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# print()
# num = 0
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             num += 1
#     print()
# print("Кол-во отрицательных элементов:", num)


# Модули

# import math   # Математика
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))
# print(math.floor(3.8))

# import math as m  # Можно заменить название
#
# print(m.ceil(3.2))
# print(m.floor(3.8))


# from math import ceil, floor  # Можно выбрать какие именно функции
#
# print(ceil(3.2))
# print(floor(3.8))


# from math import *
#
# print(ceil(3.2))
# print(floor(3.8))


# from math import pi, sqrt

# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))

# a = 8
# b = 6
# c = a ** 2 + b ** 2
# print(sqrt(c))


import time  # Время
import locale

# locale.setlocale(locale.LC_ALL, "bel")
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(893099999))
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня %B %d, %Y"))
# print(time.strftime("%B %d, %Y", time.localtime(900000000)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")


# start = time.monotonic()  # Возвращает кол-во секунд прошедших с 1970 г.
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# Функции

# def hello(name):
#     print("Hello", name)
#
#
# hello("Sobaka")
# hello("Bozik")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# num1 = 2
# num2 = 5
# res = get_sum(num1, num2)
# print(res)
# # get_sum("abc", "def")

from math import sqrt, pi


def triangle(a, b, c):
    p = (a + b + c) / 2
    res = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника:", round(res, 2))


def rectangle(a, b):
    res = a * b
    print("Площадь прямоугольника:", res)


def circle(radius):
    res = round(pi, 2) * radius ** 2
    print("Площадь круга:", res)


choice_shapes = int(input("Выберите фигуру:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n--> "))

if choice_shapes == 1:
    side_a = int(input("Введите сторону a = "))
    side_b = int(input("Введите сторону b = "))
    side_c = int(input("Введите сторону c = "))
    triangle(side_a, side_b, side_c)

if choice_shapes == 2:
    side_a = int(input("Введите сторону a = "))
    side_b = int(input("Введите сторону b = "))
    rectangle(side_a, side_b)

if choice_shapes == 3:
    circle_radius = int(input("Введите радиус окружности = "))
    circle(circle_radius)

