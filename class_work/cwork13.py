# Вложенные функции


# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer('World!')


# def func1():
#     a = 6  # 2
#
#     def func2(b):
#         a = 4  # 5
#         print(a + b)  # 6
#
#     print("a:", a)  # 3
#     func2(4)  # 4
#
#
# func1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# q = x + t
# print(q)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# Замыкание -
# когда функция возвращает другую функцию без ее вызова


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# out1 = outer(5)
# print(out1(10))
#
# out2 = outer(6)
# print(out2(4))


# def func1():
#     a = 1
#     b = "lime"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()


# Lambda - функции(выражения)


# def func(x, y):
#     return x+y
#
#
# print(func(2, 3))
#
#
# print((lambda x, y: x + y)(2, 3))

# variable = lambda x, y: x + y
#
# print(variable(2, 3))


# print((lambda a, b: a**2 + b**2)(2, 5))


# print((lambda a, b, c: a+b+c)(10, 20, 30))
# print((lambda a, b, c=3: a+b+c)(10, 20))

# print((lambda *args: sum(args))(1, 2, 3, 5, 6))
# print((lambda *args: args)("a", "b", "c"))


# tpl = (
#     lambda x: x*2,
#     lambda x: x*3,
#     lambda x: x*4,
# )
# for t in tpl:
#     print(t("abc_"))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(5)
# print(f(10))
#
#
# outer2 = lambda n: lambda x: n + x
#
# f2 = outer2(5)
# print(f(10))
# print((lambda n: lambda x: n + x)(5)(10))


# sum3 = (lambda a: lambda b: lambda c: a + b + c)
# print("sum3(2)(4)(6) =", sum3(2)(4)(6))
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))


# def func(i):
#     return i[1]
#
#
# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))


# def area_rectangle(a, b, c):
#
#     def calc_area():
#         area = 2 * (a*b + a*c + b*c)
#         return area
#
#     return calc_area
#
#
# area_rectangle_calc = area_rectangle(int(input("a:")), int(input("b:")), int(input("a:")))
# print(area_rectangle_calc())


# area = 0
#
#
# def area_rectangle(a, b, c):
#
#     def calc_area():
#         global area
#         area = 2 * (a*b + a*c + b*c)
#         return area
#
#     return calc_area
#
#
# area_rectangle_calc = area_rectangle(int(input("a:")), int(input("b:")), int(input("a:")))
# area_rectangle_calc()
# print(area)


# Оказывается надо было так =(
s = 0


def outer(a, b, c):
    global s

    def inner(i, j):
        return i * j

    s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
    return s


# print(outer(2, 4, 6))
outer(5, 8, 2)
print(s)
