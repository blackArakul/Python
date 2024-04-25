# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# else:
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# n = 2
# if n in a:
#     a.remove(n)  # удаление по значению(первое совпадение), если значения нет выбрасывает ValueError

# last = a.pop()  # удаляет последний элемент списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1)  # удаляет элемент по заданному индексу и возвращает его (IndexError) если выходим за пределы индекса
# print(second)
# print(a)
#
# a.clear()  # Очищает список от элементов
# print(a)


# n = int(input("Введите кол-во элементов списка: "))
# s = []
# for i in range(n):
#     number = int(input("-> "))
#     s.append(number)
# k = int(input("Введите индекс: "))
# s.pop(k)
# print(s)


# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)  # Считает и возвращает количество элементов в списке
# print(num)
#
# ind = a.index(3, 3, -1)  # Ищет первый элемент с введенным значением и возвращает его индекс
# print(ind)
#
# a.reverse()  # Разворачивает список в противоположенную сторону
# print(a)
#
#
# a.sort(reverse=True)  # Сортировка списка
# print(a)


# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len)
# print(s)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)

# a.sort()  # Метод изменяет сам список
# n = sorted(a, reverse=True)  # Функция не меняет исходный список, возвращает новый список, который можно сохранить в переменную
# print("n =>", n)
# print(a)


# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка id новый
# print("a", a, id(a))
# print("b", b, id(b))
# a.append(20)
# b.append(120)
# print("a", a, id(a))
# print("b", b, id(b))


# Генерация случайных данных

import random

# print(random.random())  # от 0 до 1 (не включая его)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(2, 9, 2))  # randrange(start, stop(не включая его), step)
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))  # Возвращает один элемент
# print(random.choices(city_list, k=3))  # Возвращает список элементов
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# print(random.choices(s, k=3))
#
# random.shuffle(s)  # Случайно перемешивает элементы, ничего не возвращает
# print(s)


# mas = [random.randint(0, 100) for i in range(10)]
# mas = ["a", "b", "c"]
# print(mas)
# print(max(mas))
# print(sum(mas))

# s = 0
# for i in mas:
#     s += i
# print(s)

# array = [random.randint(0, 100) for i in range(11)]
# print(array)
# max_num = max(array)
# print("Max:", max_num)
# array.remove(max_num)
# array.insert(0, max_num)
# print(array)

# array = [random.randint(-100, 100) for i in range(10)]
# print(array)
# print(sorted(array, reverse=True))

# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# min_num = min(array)
# index_num = array.index(min_num)
# print("Min:", min_num)
# print("Index:", index_num)
# del array[:index_num]
# print(array)


num_len = input("Введите кол-во элементов списка: ")
array = []
while type(num_len) != int:
    try:
        num_len = int(num_len)
    except ValueError:
        num_len = input("Введите кол-во элементов списка(ЦЕЛОЕ ЧИСЛО!): ")
for i in range(num_len):
    array_num = input("-> ")
    while type(array_num) != int:
        try:
            array_num = int(array_num)
        except ValueError:
            array_num = input("ЦЕЛОЕ ЧИСЛО! -> ")
    array.append(array_num)
num_index = input("Введите индекс: ")
while type(num_index) != int:
    try:
        num_index = int(num_index)
    except ValueError:
        num_index = input("Введите индекс (ЦЕЛОЕ ЧИСЛО!): ")
index_value = input("Введите значение: ")
while type(index_value) != int:
    try:
        index_value = int(index_value)
    except ValueError:
        index_value = input("Введите значение (ЦЕЛОЕ ЧИСЛО!): ")
array.insert(num_index, index_value)
print(array)



