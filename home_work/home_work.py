class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {self.name} должно быть целочисленное")
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD-4670K", 6, 3700],
#     "4": ["Pentium-4670K", 8, 2100],
#     "5": ["Core-4670K", 5, 6400]
# }
#
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

# num_of_symbols = input('Введите количество символов: ')
#
# while type(num_of_symbols) != int:
#     try:
#         num_of_symbols = int(num_of_symbols)
#     except ValueError:
#         num_of_symbols = input('Введите количество символов (ЦЕЛОЕ ЧИСЛО): ')
#
# type_of_symbol = input('Введите тип символа: ')
# type_of_line = input('Введите тип линии \n0 - горизонтальная\n1 - вертикальная\nОриентация линии: ')
#
# while type(type_of_line) != int:
#     try:
#         type_of_line = int(type_of_line)
#         if type_of_line == 0 or type_of_line == 1:
#             break
#         else:
#             type_of_line = input('Введите либо число НОЛЬ либо ОДИН: ')
#     except ValueError:
#         type_of_line = input('Введите либо число НОЛЬ либо ОДИН: ')
#
# i = 0
#
# if type_of_line == 0:
#     while i < num_of_symbols:
#         print(type_of_symbol, end=' ')
#         i += 1
# else:
#     while i < num_of_symbols:
#         print(type_of_symbol)
#         i += 1

#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for elem in a:
#     if elem in b and elem not in c:
#         c.append(elem)
# print(c)


