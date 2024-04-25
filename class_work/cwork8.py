# Функция для нахождения наибольшего числа

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# m = maximum(9, 6)
# print(m)


# def calculate(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return a + b
#     else:
#         print("Условие нарушено, a = b")
#
#
# num1 = int(input("a = "))
# num2 = int(input("b = "))
# print("Результат: ", calculate(num1, num2))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     # last_index = lst.pop()
#     # zero_index = lst.pop(0)
#     # lst.insert(0, last_index)
#     # lst.append(zero_index)
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# a = [1, 2, 3]
# b = [9, 12, 33, 54, 105]
# c = ["с", "л", "о", "н"]
# print("Исходные данные:\n", a, "\n", b, "\n", c)
# print("Результат:\n", change(a), "\n", change(b), "\n", change(c))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 10))
# a = 10
# b = 5
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("Ненадежный пароль")


# Типы аргументов

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))  # Именованный Параметр(аргумент) со значениями


# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(s="#")
# set_param()


# def digit_sum(n, even=True):
#     summa = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             summa += cur_digit
#         if not even and cur_digit % 2:
#             summa += cur_digit
#         n //= 10
#     return summa
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

#  Оператор is - ссылаются ли переменные на одну область памяти

# a = "Hello"
# b = "Hello"
# b = b + "_new"
# print(a, id(a))
# print(b, id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False


# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str, tuple


# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))


# Тип данных tuple(кортеж)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = "red", "blue", "green"
# print(a)
# print(type(a))

# a = (5,)
# print(a)
# print(type(a))


# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])



























