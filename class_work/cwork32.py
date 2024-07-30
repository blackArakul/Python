##############################################################
# Формат csv

# import csv

# with open("../data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {", ".join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1


#


# with open("../data.csv") as f:
#     file_names = ['Имя', "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {", ".join(row)}")
#         print(f"\t{row['Имя']} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.")
#         count += 1


#


# with open("../student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Миша", 11, 18])


#


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("../data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("../data_new.csv") as f:
#     print(f.read())


#

# with open("../student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Даша", "Возраст": 7})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 8})


#


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("../dict_writer.csv", "w") as f:
#     # fieldnames = ['hostname', 'location', 'model', 'vendor']
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
# # print(data[0].keys())


#


#############################################################
# Парсинг
#
# from bs4 import BeautifulSoup
#
# f = open("../index.html").read()
# soup = BeautifulSoup(f, "html.parser")

# row = soup.find("div", class_="name").text
# Получить текст

# row = soup.find_all("div", class_="name")

# row = soup.find_all("div", class_="row")[1].find("div", class_="links")

# row = soup.find_all("div", {"data-set": "salary"})

# row = soup.find_all("div", {"class": "name"})

# row = soup.find("div", string="Alena").parent
# Получить элемент на уровень выше

# row = soup.find("div", string="Alena").find_parent(class_="row")

# row = soup.find("div", id="whois3").find_next_sibling()
# Находит следующий элемент

# row = soup.find("div", id="whois3").find_previous_sibling()
# Находит предыдущий элемент

# print(row)


#


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# copywriter = []
# row = list(soup.find_all("div", class_="row"))
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)


#

# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# salary = soup.find_all("div", {"data-set": "salary"})
#
# for i in salary:
#     get_salary(i.text)


#
import json
import requests
import csv

response = requests.get("http://jsonplaceholder.typicode.com/todos")

todos = json.loads(response.text)
print(type(todos))

with open("../todos.csv", "w") as file:
    writer = csv.DictWriter(file, delimiter=";", fieldnames=todos[0].keys(), lineterminator="\r")
    writer.writeheader()
    for elem in todos:
        writer.writerow(elem)





