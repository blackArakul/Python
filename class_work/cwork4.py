# Вложенный цикл

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

#
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1


# Цикл for
# for element in collection(итерируемый объект):
#     print(element)

# for i in "Hello":
#     print(i)

# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)


# Функция range() - задает диапазон значений по заданным параметрам

# print(range(2, 5, 2))

# range(start, stop, step)  start = 0, step = 1 по умолчанию


# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#        # break
# else:
#     print("done")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")


# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#


# print([i * 2 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])

# Списки / list (массив в джс)

# num = [9, 3, 8, 4, 1, "Hey", 2.3, True]
# print(num)
# # print(type(num))
# # print(num[0])
# # print(num[2])
# # print(num[-1])
# # print(num[8])  # ошибка IndexError
# # num[1] = 100
# # num[2] += 50
# # num[8] = 2  # ошибка IndexError
#
# print(len(num) - 1)
# print(num[-1])


# nums = list(range(2, 21, 2))
# print(nums)

# nums = list("Hello")
# num = nums * 2
# print(num + [1, 2, 3])


# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])

# for i in nums:
#     print(i)


# Генератор списков
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)
# b = [i ** 2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in "list"]
# print(c)


# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)
#

# a = [input("-> ") for i in range(int(input("n = ")))]
# print(a)


# amount = [0] * int(input("Введите кол-во чисел последовательности: "))
# summa = 0
# for i in range(len(amount)):
#     amount[i] = input("Введите число: ")
#     try:
#         summa += int(amount[i])
#         amount[i] = int(amount[i])
#     except ValueError:
#         summa += float(amount[i])
#         amount[i] = float(amount[i])
#
# print("Кол-во чисел:", len(amount))
# print("Среднее арифметическое:", summa / len(amount))
# print("Минимальное число:", min(amount))
# print("Максимальное число", max(amount))





