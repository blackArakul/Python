##################################################
# Работа с файлами 2 часть

# file_name = "../res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = map(str, lt)  # ['4.5', '2.8', '3.9', '1.0', '0.3', '4.33',' 7.777']
#     return " ".join(lt)  # 4.5 2.8 3.9 1.0 0.3 4.33 7.777
#
#
# with open(file_name, "w") as f:
#     f.write(get_line(lst))
#
# with open(file_name, "r") as f:
#     st = f.read()
#
# nums = list(map(float, st.split()))
# print(nums)


# def long_words(file):
#     with open(file, "r", encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(long_words("../test.txt"))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("../one.txt", "w") as f:
#     f.write(text)

# with open("../one.txt", "r") as fr, open("../two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

#
#
#
###########################################################################
# Модуль OS, OS.PATH

import re
import os
# import os.path



# print(os.getcwd())  # Возвращает текущую Директорию
# print(os.listdir())  # Возвращает список директорий и файлов
# print(os.listdir(".."))  # Принимаемый аргумент возвращает список директорий и файлов с указанного пути


# os.mkdir("../folder1")  # Создает папку
# os.makedirs("../nested1/nested2/nested3")  # Создает не только конечную директорию, но и промежуточные

# os.rmdir("../folder1")  # Удаляет папку по казанному пути(пустой папки)


# os.remove("../xyz1.txt")  # Удаляет файл


# os.rename("../xyz.txt", "../new_xyz.txt")
# Переименовывает файл или папку, если во втором принимаемом аргументе указать другой путь, то перенесет его в эту директорию

# os.renames("../test.txt", "../nested1/nested3/two.txt")
# Делает тоже-самое, но если в пути указанны папки которых не существует, он их создает


# os.walk() - Возвращает кортеж в котором три элемента
# Обход дерева наоборот topdown=False
# for root, dirs, files in os.walk("../nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\t\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 30)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 30)
#
#
# remove_empty_dirs("../nested1")


# print(os.path.split(r"C:\Users\User\Desktop\Python\pythonProject\nested1\nested2\nested4\text.txt"))  # [1]
#
#
# print(os.path.join("nested4", r"C:\Users\User\Desktop\Python", "pythonProject", "nested1", "nested2", "text.txt"))


# dirs = [r"../Work\F1", r"../Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)

# files = {
#     "../Work": ["w.txt"],
#     r"../Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"../Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, "w").close()

# ../Work\w.txt
# ../Work\F1\f11.txt
# ../Work\F1\f12.txt
# ../Work\F1\f13.txt
# ../Work\F2\F21\f211.txt
# ../Work\F2\F21\f212.txt

#
# file_with_text = [r"../Work\w.txt", r"../Work\F1\f12.txt", r"../Work\F2\F21\f211.txt", r"../Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Текст в файле {file}")


root = (os.listdir(r"../nested1\nested2"))
reg = r".txt$"
res = []
for elem in root:
    if re.findall(reg, elem):
        res.insert(0, "nested2\\" + elem)
    else:
        res.append("nested2\\" + elem)
print(res)

# print(sorted(os.listdir(r"../nested1\nested2"), reverse=True))














