############################################
# Рекурсия 2 часть


# names = ["Adam", ["Bob", ["Chet", 'Cat'], "Bard", "Bert"], "Alex", ['Bea', 'Bill'], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\nWorld "))


##################################################################################
# Файлы

# f = open("../test.txt", 'r')  # "r" - режим по умолчанию
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)


#
# f = open("../test.txt", 'r')  # Относительный пусть
# # f = open(r"C:\Users\User\Desktop\Python\pythonProject\test.txt", 'r')  # Абсолютный пусть
# print(f.read(3))  # Считывает данные с файла, принимаемый аргумент считывает количество указанных символов
# print(f.read())  # При повторном вызове считывает оставшиеся символы
# f.close()

# f = open("../test2.txt", 'r')
# print(f.readline())  # Возвращает одну строку
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("../test2.txt", 'r')
# print(f.readlines(26))  # Возвращает список строк
# print(f.readlines())
# f.close()


# f = open("../test2.txt", 'r')
# for line in f:
#     print(line, end="")
# f.close()


# f = open("../test2.txt", 'r')
# # count = 0
# # for line in f:
# #     count += 1
# count = len(f.readlines())
# print(count)


# f = open("../xyz.txt", "w")
# f.write("Hello\nWorld\n")
# f.close()


# f = open("../xyz.txt", "a")
# f.write("New text.\n")
# f.close()


# f = open("../xyz.txt", "a")
# lines = ["\nThis is line 1", "\nThis is line 2"]
# f.writelines(lines)
# f.close()


# f = open("../xyz.txt", "w")
# lst = [str(i) + " " for i in range(1, 20)]
# print(lst)
# # for index in lst:
# #     f.write(index + '\t')
# f.writelines(lst)
# f.close()


# f = open("../test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()


# f = open("../test3.txt", "r")
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print()
# print(read_file)
# f.close()
#
# f = open("../test3.txt", "w")
# f.writelines(read_file)
# f.close()


# f = open("../test3.txt", "r")
# read_test = f.readlines()
# print(read_test)
# num_del = int(input("Введите индекс строки: "))
# while True:
#     if num_del < len(read_test):
#         read_test.pop(num_del)
#         break
#     else:
#         num_del = int(input("Введите корректный индекс строки: "))
# print(read_test)
# f.close()
#
# f = open("../test3.txt", "w")
# f.writelines(read_test)
# f.close()


# f = open("../test.txt", "r")
# print(f.read(3))
# print(f.tell())  # Возвращает позицию условного курсора в файле
# print(f.seek(1))  # Перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open("../test.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


##################################################
# Контекстный менеджер

# with open("../test2.txt", "w+") as f:
#     print(f.write("01234\n56789"))
# print(f.closed)


# with open("../test2.txt", "r") as f:
#     for line in f:
#         print(line[:3])


def odds_count(lst):
    if not lst:
        return 0
    else:
        if lst[0] < 0:
            return 1 + odds_count(lst[1:])
        else:
            return odds_count(lst[1:])


print(odds_count([-2, 3, 8, -11, -4, 6]))








