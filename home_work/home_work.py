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

