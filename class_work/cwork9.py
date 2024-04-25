from random import randint


# s = tuple(i for i in range(5))
# s = tuple(input("--> ") for i in range(5))
# s = tuple(2 ** i for i in range(1, 13))
# print(s)


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3 * 2)
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l1", 4))


# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, elem):
#     if elem in tpl:
#         if tpl.count(elem) > 1:
#             last_index = tpl.index(elem, tpl.index(elem) + 1) + 1
#             # return tpl[tpl.index(elem):tpl.index(elem, tpl.index(elem)+1)+1]
#             return tpl[tpl.index(elem): last_index]
#         else:
#             return tpl[tpl.index(elem):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# def generator(even=True):
#     if even:
#         return tuple(randint(0, 5) for i in range(11))
#     else:
#         return tuple(randint(-5, 0) for i in range(11))


# def generator(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = generator(0, 5)
# print(tpl1)
# tpl2 = generator(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))


# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])


# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4])
# print("Сумма:", a)
# print("Количество:", b)


# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# Тип данных Множество (set) - не упорядоченная коллекция, которая содержит только уникальные элементы (одинаковые выводятся 1 раз)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(len(s))
# print(type(s))
#
# for i in s:
#     print(i)


# s = ["banana", "apple", "orange", "banana", "apple"]
# print(s)
# st = set(s)
# print(st)
# lst = list(st)
# print(lst)


# a = set("Hello")
# print(type(a))
# print(a)


# s = {input("--> ") for i in range(5)}
# print(s)


# a = set("Hello")
# print(a)
# print("o" in a)
# print("a" in a)
# a.add("a")
# print(a)
# el = "e1"
# if el in a:
#     a.remove(el)  # KeyError
# print(a)
# a.discard("o")  # Не выбрасывает исключение, если элемента нет
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)


# def num_count(tpl):
#     array = []
#     over = "Программа подсчета завершена"
#     for elem in tpl:
#         if elem in tpl and elem not in array:
#             array.append(elem)
#             print("Количество:", elem, "=", tpl.count(elem))
#     return over
#
#
# tuple_array = tuple(input("Введите элементы кортежа: "))
# print(tuple_array)
# print(num_count(tuple_array))

