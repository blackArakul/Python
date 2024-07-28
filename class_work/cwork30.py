#################################################
# Упаковка и распаковка данных
# # Сериализация
# # Десериализация


# marshal (*.pyc)
# pickle (работает только в пайтон)
# json (из почти любого языка)

################################################
# import pickle


# file_name = "../basket.txt"
# shop_list = {
#     "фрукты":  ("яблоки", "манго"),
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
#
# with open(file_name, "rb") as f:
#     shop_list2 = pickle.load(f)
#
# print(shop_list2)


# class Text:
#     num = 35
#     string = "Hello"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Text.num}\nСтрока: {Text.string}\nСписок: {Text.lst}\nКортеж: {Text.tpl}"
#
#
# obj = Text()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# obj2 = pickle.loads(my_obj)
# print(obj2)


#


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
#
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


#


############################################################
import json
import random

# data = {
#     'name': 'Ольга',
#     'age': 20,
#     20: None,
#     True: 1,
#     'hobbies': ('running', "singing"),
#     "children": ['Alice', "Bob"]
# }
#
# with open('../data_file.json', "w") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
#
# with open('../data_file.json') as f:
#     data1 = json.load(f)
#
# print(data1)

# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# print(type(json_string))
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))


#
from random import choice

#
# def gen_person():
#     name = ""
#     tel = ""
#
#     letters = ["a", "b", "c", "d", "e", "f", "g"]
#     nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("../persons.json"))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open("../persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


#


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Студент: {self.name} => {", ".join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def dell_mark(self, mark_index):
        del self.marks[mark_index - 1]

    def edit_mark(self, index, new_mark):
        self.marks[index - 1] = new_mark

    def average_marks(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_file_name(self):
        return self.name.lower() + ".json"

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(f"../{self.get_file_name()}", "w") as file:
            json.dump(data, file, indent=2)

    def load_from_file(self):
        with open(f"../{self.get_file_name()}") as file:
            print(json.load(file))


class Group:
    def __init__(self, students, group_name):
        self.students = students
        self.group_name = group_name

    def __str__(self):
        return f"Группа: {self.group_name}\n{"\n".join(map(str, self.students))}"

    def add_student(self, new_student):
        self.students.append(new_student)

    def del_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(gr1, gr2, index):
        gr2.add_student(gr1.del_student(index))

    def get_file_name(self):
        return self.group_name.lower().replace(" ", "-") + ".json"

    def dump_to_json(self):
        data = [
            {"name": student.name, "marks": student.marks} for student in self.students
        ]
        with open(f"../{self.get_file_name()}", "w") as file:
            json.dump(data, file, indent=2)

    def load_file(self):
        with open(f"../{self.get_file_name()}") as f:
            print(json.load(f))

    @staticmethod
    def dump_to_json_groups(the_group):
        try:
            data = json.load(open("../groups.json"))
        except FileNotFoundError:
            data = dict()
        gr_dict = {
            the_group.group_name: [
                {student.name: student.marks} for student in the_group.students
            ]
        }
        data.update(gr_dict)
        with open("../groups.json", "w") as groups:
            json.dump(data, groups, indent=2)


# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.dell_mark(3)
# print(st1)
# st1.edit_mark(3, 5)
# print(st1)
# print(st1.average_marks())
# st1.dump_to_json()
# st1.load_from_file()
#
#
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st2.dump_to_json()


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts1 = [st1, st2]
group1 = Group(sts1, "ГК Python")
# print(group1)
# print()
group1.add_student(st3)
# print(group1)
# print()
group1.del_student(2)
# print(group1)
# print()

sts2 = [st3]
group2 = Group(sts2, "ГК Web")
# print(group2)

Group.change_group(group1, group2, 0)
# print()
# print(group1)
# print()
# print(group2)
# group2.dump_to_json()

# group2.load_file()
# group2.dump_to_json_groups()
# group1.dump_to_json_groups()
# Group.dump_to_json_groups(group2)
# Group.dump_to_json_groups(group1)

