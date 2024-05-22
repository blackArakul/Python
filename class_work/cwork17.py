###############################
# Регулярные выражения

# import re
#
# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "а"
#
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения
# # Если совпадений нет, вернет пустой список
#
# print(re.search(reg, s))  # местоположение первого совпадения с объектом
# # print(re.search(reg, s).span())  # кортеж индексов start end
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())  # само совпадение
#
#
# print(re.match(reg, s))  # Поиск совпадения с шаблоном в начале строки
#
#
# print(re.split(reg, s, 1))  # Возвращает список в котором строка разбита по шаблону
#
#
# print(re.sub(reg, "!", s, 2))  # поиск и замена


import re

# s = "Я ищу совпадение в 2024 году. И я их  [найду] в 2 счёта. 98673 Hello"
# reg = "[12][0-9][0-9][0-9]"
# reg = "[]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]"
# reg = r"[^А-яЁёA-Za-z0-9]"
# print(re.findall(reg, s))

# print(ord("я"))
# print(ord("ё"))

#
# test = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
#
# reg = "[0-2][0-9]:[0-5][0-9]"
#
# print(re.findall(reg, test))

#
# s = "Я ищу совпадение в 2024 году. И я их  [найду] в 2 счё-та. 198673 Hel_lo"
# reg = r"[20]*"
# print(re.findall(reg, s))

# Количество повторений
# + от 1 до бесконечности
# * от 0 до бесконечности
# ? от 0 до 1


# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r'[+-]?[\d+.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# # print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print("Дата рождения:", re.sub("-", ".", re.sub(r"\s#.*", "", s)))


# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r"\w+\s*=\s*[^;]+"
# # reg = r"[^;]+"
# print(re.findall(reg, s))


# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}$", login)
#
#
# print(validate_login("Python-master"))

test = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
reg = r"[+]?\d{11,}"
print(re.findall(reg, test))















