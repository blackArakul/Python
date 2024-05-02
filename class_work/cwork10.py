# s = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = [x for x in s if "a" not in x]
# a = ["A" + x[1:] if x[0] == "a" else "B" + x[1:] for x in s]
# a = ["A" + x[1:] if x[0] == "a" else "B" + x[1:] for x in s if x[1] == "c"]
# print(a)


# Тернарное выражение q = True if условие else False


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# # c = a.union(b)  # Возвращает множество, объединением множеств
# c = a | b
# print(c)

# # a.update(b)  # Добавляет в множество а все элементы b
# a |= b
# print(a)

# # c = a.intersection(b)  # Возвращает пересечение множеств
# c = a & b
# print(c)

# # a.intersection_update(b)  # Оставляет в а те элементы, которые есть в b
# a &= b
# print(a)

# # c = a.difference(b)  # Возвращает элементы входящие в одно множество, но не входящие в другое
# c = a - b
# print(c)

# # a.difference_update(b)  # Удаляет из а все элементы b
# a -= b
# print(a)

# # c = a.symmetric_difference(b)  # Возвращает уникальные элементы из множеств
# c = a ^ b
# print(c)

# # a.symmetric_difference_update(b) # Перезаписываем в а уникальные элементы из двух множеств
# a ^= b
# print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # c = s1.union(s2, s3, s4, s5, s6, s7)
# c = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(c)
# print(len(c))
# print("Min elem:", min(c))
# print("Max elem:", max(c))


# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# print("Только одно хобби:", drawing ^ music)
# print("Два хобби:", drawing & music)
# print("Рисование:", drawing - music)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a < b)


# Тип данных frozenset - неизменяемый тип данных, замороженное множество


# # s = frozenset([1, 2, 3, 4, 5, 6])
# s = frozenset("Hello")
# print(s)


# Словари (dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])
#
# s1 = ["one", "two", "three"]
# d1 = {1: "one", 2: "two", 3: "three"}
# print(s1[1])
# print(d1[2])


# d = {0: "test", "one": 45, (1, 2.3): "Кортеж", True: 1,  35: {2, 3, 6, 7}, False: "один",}
# print(d)
# # Ключами могут быть, только неизменяемы типы данных
# # Ключи не могут повторятся
# d[(1, 2.3)] = 100
# print(d)


# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))


# d1 = dict(Мгер=1, two=2)
# print(d1)
# print(type(d1))


# d1 = dict([("one", 1), ("two", 2)])
# print(d1)


# d = {x: x ** 2 for x in range(7)}
# print(d)


# d = {"one": 1, "two": 2, "three": 3}
# print("two" in d)
# print(2 in d)  # in поиск только по ключам
# print(len(d))

# for key in d:
#     print(key, "->", d[key])

# key = "one"   # "four"
# del d[key]
# print(d)
# if key in d:  # Защита от ошибок
#     print(d[key])

# try:
#     print(d[key])
# except KeyError:
#     print("Такого ключа не существует")


# dicta = dict(x1=3, x2=7, x3=5, x4=-1)
# res = 1
# for key in dicta:
#     res *= dicta[key]
# print(res)


# dicti = {x: input("Введите название овоща: ") for x in range(1, 5)}
# print(dicti)
# try:
#     deleted = int(input("Введите число элемента, который нужно исключить: "))
#     del dicti[deleted]
# except (KeyError, ValueError):
#     print("Такого ключа не существует")
# print(dicti)


winners_math = ["Natalia", "Maxim", "Evgeniya", "Matvei", "Michail"]
winners_physics = ["Maxim", "Matvei", "Alexandr"]
winners_in_tow_disciplines = set(winners_math) & set(winners_physics)
print("Все призеры", list(set(winners_math) | set(winners_physics)))
print("Призеры обеих олимпиад", winners_in_tow_disciplines)
print("Обновленный список по математике:", set(winners_math) & winners_in_tow_disciplines)


















