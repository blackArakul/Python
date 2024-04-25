# num = 4321
# a = num % 10
# print(a)  # 1 последнее число
# num = num // 10  # 432,1  - 1 отбрасывается
# # print("num:", num)
# b = num % 10
# print(b)  # 2
# num = num // 10
# # print("num:", num)
# c =
# print(c)  # 3
# num = num // 10
# # print("num:", num)
# d = num % 10
# print(d)  # 4
# num = a * 1000 + b * 100 + c * 10 + d
# print(num)


# num = 9753
# res = num % 10 * 1000  # 100
# num //= 10  # 432
# res += num % 10 * 100  # 200
# num //= 10  # 43
# res += num % 10 * 10  # 30
# num //= 10  # 4
# res += num % 10
# print(res)

#
# print(int(3.8))  # 3
# a = round(3.8464545, 2)  #  второй параметр кол-во символов после запятой , вещественное число
# print(round(3.8454545))  # 4 от 0.5 и выше округление в высшую сторону
# print(a, type(a))


# a = "5.2"
# b = 10
# c = int(a) + b
# print(c)


# name = "Viktor"
# age = 28
# print("My name", name, ". Mne", age, "years")
# print("My name " + name + ". Mne " + str(age) + " years")
# print("My name", name, ". Mne", age, "years.", sep="---", end="\n\n")  # заменяет символ запятой
# print("hello")


# name = input("Введите имя: ")  # Возвращает str
# city = input("Введите город: ")
# print(name, city)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, " равно", res)


# num1 = int(input("Введите число 1:"))
# num2 = int(input("Введите число 2:"))
# num3 = int(input("Введите число 3:"))
# num4 = int(input("Введите число 4:"))
#
# # add1 = num1 + num2
# # add2 = num3 + num4
# # res = add1 / add2
# # res = round(res, 2)
# res = round((num1 + num2) / (num3 + num4), 2)
# print(res)


# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5
# print(type(b1))


#  False => "", 0, 0.0, False, None

# print(bool("python"))
# print(bool(""))
# print(bool(10))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
#
# test = None
# print(type(test))
# test = 5
# print(test)


# print(7 == 7)
# print(7 == "7")
# print(2 + 5 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print("привет" > "ПРИВЕТ")  # 175 > 143 код 1 символов


# print(2 < 4 < 9)  # True : True => True
# print(2 < 4 > 9)  # True : False => False
# print(2 * 5 > 7 >= 4 + 3)  # True : True => True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False


# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 < 2 or 1 + 3 < 4)  # False or False => False
# print(not 9 - 5)  # False
# print(not 9 - 9)  # True


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# PEP20
# import this


# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")


# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or c == a:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("четверг")
#     if day == 4:
#         print("среда")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")


# n = int(input("Введите кол-во ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


num = int(input("Введите число (от 1 до 99) "))
second_num = num % 10
if 1 <= num <= 99:
    if 11 <= num <= 14:
        print(num, "копеек")
    elif second_num == 1:
        print(num, "копейка")
    elif 5 <= second_num <= 9 or second_num == 0:
        print(num, "копеек")
    elif 2 <= second_num <= 4:
        print(num, "копейки")
else:
    print("Ошибка ввода числа")
