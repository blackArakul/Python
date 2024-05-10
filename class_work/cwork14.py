# players = [
#     {"name": "Aнтон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6}
# ]
#
# players.sort(key=lambda item: item["last name"])
# print(players)
# players.sort(reverse=True, key=lambda item: item["rating"])
# print(players)
# players.sort(key=lambda item: item["rating"])
# print(players)


# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# res = a[0](7, 8)
# print(res)


# dicti = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# dicti[3]()


# print((lambda a, b: a if a > b else b)(5, 3))


# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(12, 2, 1))
#
# print((lambda *args: min(args))(2, 5, 6))
#
# print((lambda *args: sorted(args)[0])(12, 5, 6))


# Циклы в одну строку map(func, iterable), filter(func, iterable)######

# map() #########


# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lt = list(map(mult, lst))
# print(lt)
#
# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))


# lst = ["1", "2", "3", "4", "5"]
# print(lst)
#
# print(list(map(lambda x: int(x), lst)))
# print([int(i) for i in lst])
# print(list(map(int, lst)))


# st = ["a", 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x, y: (x, y), st, num)))
#
# st = [9, 8, 7, 6, 5]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))


# filter() ######### Как будто цикл и условие


# t = ('abcd', 'abc', 'cdefg', 'def', 'gth')
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# t2 = tuple(filter(lambda s: s * 3, t))
# print(t2)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# print(list(filter(lambda x: x >= 75, b)))

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print("[10; 20] =", list(filter(lambda x: 10 <= x <= 20, lst)))


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы #######

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
#
# print(test())
# print(id(test))
# print(id(hello))


# def my_decorator(func):
#
#     def inner():
#         print("Code Before")
#         func()
#         print('Code after')
#
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")


# test = my_decorator(func_test)
#
# test()

# def my_decorator(func):  # декорирующая функция
#
#     def inner():
#         print("*" * 28)
#         func()
#         print('*' * 28)
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


words = ['madam', 'fire', 'tomato', 'book', 'kiosk', 'mom']

print(list(filter(lambda elem: elem == elem[::-1], words)))


