#####################################################################
# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def del_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print("\nТакой страны в базе нет!\n")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"\nСтрана {country.capitalize()} столица  {data[country].capitalize()} есть в словаре\n")
#         else:
#             print(f"\n{country.capitalize()} в базе нет\n")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             new_capital = input("Введите новое значение столицы: ").lower()
#             data[country] = new_capital.capitalize()
#             with open(file_name, "w") as f:
#                 json.dump(data, f, indent=2)
#         else:
#             print(f"\n{country.capitalize()} нет в базе\n")
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print("\n", {key.capitalize(): value.capitalize() for key, value in json.load(f).items()}, "\n")
#
#
# file = "../list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n"
#                   "3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n"
#                   "завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.del_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("\nВведен некорректный номер!\n")


#


import requests
import json

response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1  # todo["userId"] создает ключ по его значению
        except KeyError:
            todos_by_user[todo["userId"]] = 1
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]

max_complete = top_users[0][1]  # 12
print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:  # 12 < 12
        break
    users.append(str(user))  # [5, 10]
print(users)

print(f"users {" and ".join(users)} completed {max_complete} Todos")

filter_max_user = []

for user in todos:
    if user["completed"]:
        if user["userId"] == 5 or user["userId"] == 10:
            filter_max_user.append(user)

with open("../filter_max.json", "w") as f:
    json.dump(filter_max_user, f, indent=2)













