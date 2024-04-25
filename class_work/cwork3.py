# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin1"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль неверный")


# day = "вторник"
# time = 17
#
# match day:
#     case "Понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "Суббота" | "Воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# Тернарное выражение

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 20, 10
# print(a / b if a > 0 and b > 0 else "На ноль делить нельзя")


# Исключения / Exception

# a = 5
# b = 0
# print(a / b)
# NameError - не найдена такая переменная
# TypeError - операция несоответствующему типу данных
# ValueError - синтаксис или функция получают аргумент, тип которой правильный, но не правильно значение
# ZeroDivisionError - возникает, когда второй аргумент равен 0


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на 0")
# else:  # Отрабатывает когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # Выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)  # "строка" => число
#     m = int(m)
#     print(n + m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# x = input("Введите первое число: ")
# y = input("Введите второе число: ")
# try:
#     print(int(x) + int(y))
# except ValueError:
#     print(x + y)


# Цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1


# n = int(input("Укажите кол-во символов "))
# print("*" * n)


# n = int(input("Укажите кол-во символов "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Укажите кол-во символов "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)


# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         print("Идите нахуй")
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         print("Результат:", res)
#         break
#     res *= n


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# Вложенный цикл

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1

symbol_num = int(input("Кол-во символов: "))
symbol_type = input("Тип символа: ")
print("0 - горизонтальная")
print("1 - вертикальная")
symbol_orient = int(input("Ориентация линии: "))
i = 0

while i <= symbol_num:
    if symbol_orient == 1:
        print(symbol_type)
    elif symbol_orient == 0:
        print(symbol_type, end=" ")
    else:
        print("Ошибка ввода")
        break
    i += 1
