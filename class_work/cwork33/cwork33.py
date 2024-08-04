###############################################################
# Парсинг

import csv
import re
import requests
from bs4 import BeautifulSoup


# r = requests.get("https://ru.wordpress.org/")
# print(r.content)  # Возвращает байтовую строку
# print(r.status_code)  # Возвращает код состояния
# print(r.headers)  # Возвращает заголовки сервера
# print(r.headers["content-type"])  # Возвращает значения по ключу
# print(r.text)  # Возвращает строку с элементами интернет ресурса


#


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("main", class_="wp-block-group entry-content is-layout-constrained wp-container-core-group-is-layout-19 wp-block-group-is-layout-constrained").find("h1", class_="wp-block-heading").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == "__main__":
#     main()


#


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind(st):
#     res = re.sub(r"\D+", "", st)
#     return res
#
#
# def write_csv(data):
#     with open("../plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[-1]
#     plugins = p1.find_all("li")
#
#     for block in plugins:
#         name = block.find("h3").text
#         url = block.find("h3").find("a").get("href")
#         rating = block.find("span", class_="rating-count").text.strip("(").strip(")")
#         ref = refind(rating)
#         data = {"name": name, "url": url, "rating": ref}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()
#


#


#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(st):
#     return st.split()[-1]
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("li", class_="wp-block-post")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except Exception as e:
#             name = ""
#             print(e)
#
#         try:
#             url = el.find("h3").find("a")["href"]
#         except Exception as e:
#             url = ""
#             print(e)
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except Exception as e:
#             snippet = ""
#             print(e)
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             tested = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(tested)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'tested': cy
#         }
#
#         write_csv(data)
#
#
# def write_csv(data):
#     with open("../plugins1.csv", "a", encoding="windows-1251")as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data['name'], data['url'], data['snippet'], data['active'], data['tested']])
#
#
# def main():
#     for i in range(24, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


from pars_ebidaebi import Parser


def main():
    pars = Parser("https://krasnodar.yobidoyobi.ru/vkusy-18", "menu.csv")
    pars.run()


if __name__ == '__main__':
    main()









