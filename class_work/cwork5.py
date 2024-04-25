#
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# summa = 0
# for i in range(len(a)):
#     try:
#         a[i] = int(a[i])
#     except ValueError:
#         a[i] = float(a[i])
#     if a[i] < 0:
#         summa += a[i]
# for i in a:
#     if i < 0:
#         summa += i
# print(summa)


# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):  # i = 0 1 2 3 4 5 6 7 8
#     print(lst[i], end=" ")
# print()
# for i in lst:  # i = 10 20 30 40 50 60 70 80 90
#     print(i, end=" ")

# colors = ["red", "blue", "green"]
# for i in range(len(colors)):  # i = 0 1 2
#     print(colors[i], end=" ")
# print()
# for i in colors:  # i = red, blue, green
#     print(i, end=" ")


# num = list(range(21, 41))
# count = sum1 = 0
# for i in num:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum1 += i
#
# print(num)
# print("Кол-во четных чисел:", count)
# print("Сумма нечетных чисел:", sum1)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# for i in a:
#     if i > i - 1:  # не корректно
#         print(i, end=" ")


# a = [7, 9, 3, 1, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)


# Срезы - получение какой-то части списка, которая тоже будет являться списком
# список[старт:стоп(не включая его):степ]

# s = [5, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[0:4]
# print(b, id(b))


# s = "Hello World!"
# print(s[6:11])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20, 30]
# print(s)
# s[2] = 50
# print(s)
# Если изменяем по индексу , то записываем один элемент
# Если несколько, то получится картеж
# Если по срезу, то добавляем только список
# s[3:6] = []
# print(s)
# del s[1:3]  # del - универсальная функция для удаления
# print(s)


# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# s[len(s):] = [12]
# print(s)


# Методы списков
# dir(list)
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# s.append(12)  # Добавляет один элемент в конец списка
# print(s)
# s.append([1, 2, 3])
# print(s)
#
# s.extend([1, 2, 3])  # Добавляет любое кол-во элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
#
# s.insert(3, "Hello")  # добавляет элемент в список заданный индекс и передаем значение
# print(s)
# s.insert(20, 90)  # лучше не пользоваться
# print(s)


# s = []
# n = int(input("Введите кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# for elem in a:
#     if elem not in c and elem in b:
#         c.append(elem)
# print(c)


# number = int(input("Введите кол-во элементов списка: "))
# array = []
#
# for elem in range(number):
#     num3 = int(input("Введите число кратное 3: "))
#     if num3 % 3 == 0:
#         array.append(num3)
#     else:
#         print(num3, "не делится на 3 без остатка")
# print(array)


number = input("Введите кол-во элементов списка: ")
array = []

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        number = input("Введите кол-во элементов списка (Целое число!): ")

for elem in range(number):
    num3 = input("Введите число кратное 3: ")
    while type(num3) != int:
        try:
            num3 = int(num3)
        except ValueError:
            num3 = input("Введите число кратное 3 (Целое число!): ")
    if num3 % 3 == 0:
        array.append(num3)
    else:
        print(num3, "не делится на 3 без остатка")
print(array)










