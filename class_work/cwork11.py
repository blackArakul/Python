
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD-4670K", 6, 3700],
#     "4": ["Pentium-4670K", 8, 2100],
#     "5": ["Core-4670K", 5, 6400]
# }
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], " руб.", sep="")
#
# while True:
#     num = input("Введите номер: ")
#     if num != "0":
#         if num in goods:
#             while True:
#                 try:
#                     count = int(input("Введите количество: "))
#                     goods[num][1] += count
#                     break
#                 except ValueError:
#                     print("Введите ЦЕЛОЕ ЧИСЛО!")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
#
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], "шт. по ", goods[key][2], " руб.", sep="")


# dicti = dict(x1=3, x2=7, x3=5)
# print(dicti)
# # del dicti["x1"]
# # dicti["x4"] = 10
# # print(dicti)
###
# print(dicti.values())  # Список значений
# print(dicti.keys())  # Список ключей
# print(dicti.items())  # Список из кортежей со значениями
###
# # for key, value in dicti.items():
# #     print(key, "-", value)
# print(list(dicti))  # Получим список ключей
# print(list(dicti.values()))  # Возвращает список значений
# print(list(dicti.items()))  # Возвращает список из кортежей с ключами и значениями


# dicti = dict(x1=3, x2=7, x3=5)
#
# d2 = dicti.copy()
# print("dicti =", dicti)
# print("d2 =", d2)
#
# d2["x4"] = 10
# dicti["x1"] = 100
# print("dicti =", dicti)
# print("d2 =", d2)

# dicti = dict(x1=3, x2=7, x3=5)
# print(dicti)
# print(dicti["x1"])
#
# value = dicti.get("x1", "Такого ключа не существует")
# # Получает значение ключа, если ключа нет, возвращает второй параметр, если второго парам нет, возвращает None
# print(value)

# item = dicti.pop("x4", 0)
# # Возвращает значение ключа и удаляет ключ целиком, если ключа нет, возвращает второй параметр
# print(item)
# print(dicti)

# item2 = dicti.popitem()
# # Удаляет последний элемент словаря и возвращает кортеж ключа и значение
# print(item2)
# print(dicti)
#
#
# dicti.clear()
# print(dicti)


# dicti = dict(x1=3, x2=7, x3=5)
# print(dicti)
# item = dicti.setdefault("x4", 10)
# # Добавлять новый ключ с новым значением
# print(item)
# print(dicti)


# a = dict(one=1, two=2)
# print(a)
# a = list(a.items())
# dicti.update(a)
# print(a)
# # Добавляет в словарь элементы другого
# print(dicti)


# dic = dict.fromkeys(["a", "b", "c"],  100)
# # Пишутся ключи и одно значения для всех ключей
# print(dic)


# dic = {"name": "Kelly", "age": 25, "salary": "8000", "city": "New York"}
# dic2 = dict()
# dic2["name"] = dic.pop("name")
# dic2["salary"] = dic.pop("salary")
# print(dic)
# print(dic2)


# dic = {"name": "Kelly", "age": 25, "salary": "8000", "city": "New York"}
# dic["location"] = dic.pop("city")
# print(dic)


# dic = {
#     "first": {
#         1: "one",
#         2: 'two',
#         3: {
#             11: "abc"
#         }
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(dic)
#
# for x in dic:
#     print(x)
#     for y in dic[x]:
#         print("\t", y, ": ", dic[x][y], sep="")
#         for z in dic[x][y]:
#             print("\t", z, ":", dic[x][y][z])


# dic = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # dic2 = {value: key for key, value in dic.items()}
# # # Генератор списка, меняем местами ключ и значение
# # print(dic2)
#
# dic2 = {key: value for key, value in dic.items() if value <= 2}
# print(dic2)

# lis = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# dic = dict()
# key = None
# for elem in lis:
#     if type(elem) is str:
#         dic[elem] = []
#         key = elem
#     else:
#         dic[key].append(elem)
# print(dic)


dict_sell = {
    "John": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694,
    },
    "Tom": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694,
    },
    "Anne": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694,
    },
    "Fiona": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694,
    }
}

# for x in dict_sell:
#     print(x)
#     for y in dict_sell[x]:
#         print("\t", y, ":", dict_sell[x][y])

while True:
    print("Что бы выйти из приложения наберите exit")
    name_seller = input("Введите имя продавца: ")
    if name_seller != "exit":
        if name_seller in dict_sell:
            region_seller = input("Введите регион(N,S,E,W): ")
            if region_seller in dict_sell[name_seller]:
                print(dict_sell[name_seller][region_seller])
                while True:
                    try:
                        num_of_sales = int(input("Введите новое значение продажи: "))
                        dict_sell[name_seller][region_seller] = num_of_sales
                        print(dict_sell[name_seller])
                        break
                    except ValueError:
                        print("Новое значение продаж должно быть ЦЕЛОЕ ЧИСЛО")
            else:
                print("Такого региона не существует")
        else:
            print("Такого имени не существует")
    else:
        break






