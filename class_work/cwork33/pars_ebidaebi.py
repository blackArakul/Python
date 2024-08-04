import requests
from bs4 import BeautifulSoup
import csv
import re


class Parser:
    html = ""

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        menu = self.html.find_all("div", class_="mChQYM")
        for elem in menu:
            try:
                title_elem = re.match(r'^[^0-9]+', elem.find("div", class_="_3bobQZ").find("h3").text)
                title = title_elem.group(0)
            except Exception as e:
                title = ""
                print(e)

            try:
                description = elem.find("div", class_="_3bobQZ").find("p").text.strip()
            except Exception as e:
                description = ""
                print(e)

            try:
                price = elem.find("div", class_="GWFgdO").find("p").text.strip()[:-1]
            except Exception as e:
                price = ""
                print(e)
            data = {
                "title": title,
                "description": description,
                "price": price
            }
            self.write_csv(data)

    def write_csv(self, data):
        try:
            with open(self.path, "a", encoding="windows-1251") as f:
                writer = csv.writer(f, delimiter=";", lineterminator="\r")
                writer.writerow([data["title"], data["description"], data["price"]])
        except Exception as e:
            print(e)

    def run(self):
        self.get_html()
        self.parsing()









