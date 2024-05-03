# Функция zip()
# Создает пару по минимальному количеству элементов
# Если 2 списка в список - список кортежей
# Если 2 списка в словарь - zip(ключ, значение) не больше 2ух передаваемых параметров


# one = [1, 2, 3, 4, 5]
# two = ["one", "two", "three"]
# # three = [2.5, 4.6, 8.9]
# d = dict(zip(one, two))
# print(d)
#
# # lst = list(zip(one, two, three))
# lst = list(zip(one))
# print(lst)


# f = {k: v for k, v in zip(two, one)}
# print(f)


# one = {"name": "Igor", "surname": "Doe", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Smith", "job": "Manager"}
#
# for (key1, value1), (key2, value2) in zip(one.items(), two.items()):
#     print(key1, "->", value1)
#     print(key2, "->", value2)

# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*lst)  # Распаковка последовательностей
# print(a)  # (1, 2, 3)
# print(b)  # ('one', 'two', 'three')


# a = {"one": 1, "two": 2, "three": 5}
# b = {"three": 3, "four": 4}
# print({**a, **b})  # Объединение словарей
#
# for k, v in {**a, **b}.items():
#     print(k, "->", v)


# # enumerate(коллекция, начало нумерации) #
# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# data = ["red", "green", "blue"]
#
# for num, color in enumerate(data, 1):
#     print(num, ") ", color, sep="")


# j = 1
# for i in data:
#     print(j, ") ", i, sep="")
#     j += 1


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, "abc"))


# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(summa(1, 3, 45, 45, 45, 45, 45, 54, 5, 45, 45, 4, 54, 5, 2))
# print(summa(4, 2, 6))
# print(max(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def to_dict(*args):
#     # dic = {elem: elem for elem in args}
#     return dict(zip(args, args))
#
#
# print(to_dict(1, "пуц", 2.5, (9, 9, 8), -25))


# def arif(*args):
#     lst = []
#     print(sum(args) / len(args))
#     for num in args:
#         if num < (sum(args) / len(args)):
#             lst.append(num)
#     return lst
#
#
# print(arif(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(arif(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 9, 8, 7, 6))


# def print_scores(student, *scores):
#     print("Name:", student)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Roman", 5, 4, 3, 5, 4, 5, 5, 3, 5)
# print_scores("Nikita", 5, 5, 3, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Python"))


# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(key, "is", value)
#     print()
#
#
# intro(name="Irina", surname="Shmara", age=22)
# intro(name="Issa", surname="Ahtari", email="issa@gmail.com", age=22, phone=98123761523)


# def func(a, *args, dd=5, cc=7, **kwargs):
#     return a, args, kwargs, dd, cc
#
#
# print(func(1, 2, 3, 4, 5, aa=1, bb=2, cc=3))


# def update_dict(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# update_dict(k1=22, k2=31, k3=11, k4=91)
# update_dict(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)


# name = "Tom"  # глобальная переменная
# surname = None
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# x = 10
#
#
# def func(a):
#     # x = 2
#
#     def inner():
#         # x = 6
#         print("x:", x)
#         return a + x
#
#     return inner()
#
#
# print(func(3))

students = {input(str(i + 1) + "-й студент: "): int(input("Балл: ")) for i in range(int(input("Количество студентов: ")))}

res = round(sum(students.values()) / len(students))

print("Средний балл: ", res, ". Студенты с баллом выше среднего: ", sep="")
for key, value in students.items():
    if value > res:
        print(key)








