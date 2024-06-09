##################################################################################
# Работа с файлами часть 3

# import os


# print(os.path.isfile(r"../nested1/nested2/test2.txt"))
# # Возвращает Boolean значение, если путь является файлом
#
# print(os.path.isdir(r"../nested1/nested2"))
# # Возвращает Boolean значение, если путь является папкой(Директорией)


# root = r"../nested1\nested2"
# objects = os.listdir(root)
# objects = list(map(lambda i: os.path.join(root, i), objects))
# # print(objects)
#
# sort_objects = sorted(objects, reverse=True)
# print(sort_objects)

#


# print(os.path.exists(r"../nested1/nested2/test2.txt"))
# # Возвращает Boolean значение, существует ли путь к фалу или папке
#
# print(os.path.getsize("cwork2.py"))
# # Возвращает размер (файла, папки) в байтах

#
# b = os.path.getsize(r"cwork2.py")
# print(b, "байт")
# print(b // 1024, "килобайт")

#
# import time
#
#
# path = "cwork3.py"
# print(os.path.getctime(path))  # возвращает время создания файла (в секундах)
# print(os.path.getatime(path))  # возвращает последнее время доступа к файлу (в секундах)
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла (в секундах)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path))))
#
#
#
#
#
#
###################################################################
# ООП


# class Point:
#     """Класс для предоставления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()  # экземпляр класса
# print(p1.x)
# print(type(p1))
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Point:
#     x = 1
#     y = 1


# p1 = Point()
# p1.x = 10
# p1.y = 20
# p1.z = 30
# print(p1.x, p1.y, p1.z)
# print(p1.__dict__)  # Возвращает словарь измененных значений
#
#
# p2 = Point()
# p2.x = 100
# print(p2.x, p2.y)
# print(p2.__dict__)
# # print(f"{id(Point())}\n{id(p1)}\n{id(p2)}")
#


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
#
# p2 = Point()
# # p2.x = 50
# # p2.y = 100
# p2.set_coord(50, 100)

#
# class Human:
#     name = "name"
#     birthday = "00.00.00"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата Рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить время
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("23.12.1990")
# print(h1.get_birthday())
# h1.print_info()


# class Person:
#     qualification = 10  # Статическое свойство
#     count = 0
#
#     def __init__(self, name, last_name):  # Инициализатор(магический метод)
#         # Срабатывает в момент создания экземпляра класса
#         self.name = name            #
#         self.last_name = last_name  # Динамические свойства
#         Person.count += 1
#
#     def __del__(self):  # Финализатор (деструктор)
#         print(f"Удаление экземпляра: {self.__class__.__name__}")
#
#     def print_info(self):
#         print(f"Данные сотрудника: {self.name} {self.last_name}")
#
#     def add_qualification(self, qualif):
#         self.qualification += qualif
#         print(f"Квалификация сотрудника: {self.qualification}", end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_qualification(2)
# # del p1
# # p1 = 5
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_qualification(5)
# print(p2.count)
# print(Person.count)


class Car:
    def __init__(self, car_name, year_release, car_maker, engine_power, car_color, price):
        self.car_name = car_name
        self.year_release = year_release
        self.car_maker = car_maker
        self.engine_power = engine_power
        self.car_color = car_color
        self.price = price

    def print_info(self):
        print("Данные автомобиля".center(40, "*"))
        print(f"Название модели: {self.car_name}\nГод выпуска: {self.year_release}\nПроизводитель: {self.car_maker}\nМощность двигателся: {self.engine_power}\nЦвет машины: {self.car_color}\nЦена: {self.price}")
        print("=" * 40)

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return "Цена:" + self.price


instance_car = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
instance_car.print_info()
instance_car.set_price("255555555")
instance_car.print_info()
print(instance_car.get_price())







