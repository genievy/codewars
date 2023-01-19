import time
#
# def func_time(n):
#     d = []
#     start = start_time = time.clock()
#     for i in range(n):
#         d.__setitem__('i', )
#     print(time.clock() - start_time, "seconds")
#     return d

# def func_time(n):
#     start = start_time = time.clock()
#     s = [0]*n
#     for i in range(n):
#         s[i] = i
#     print(time.clock() - start_time, "seconds")
#     print(len(s))
#     return s
#
# func_time(20000000)


# def div_min_max(n):
#     l =[]
#     for i in range(1, 10000000):
#         if n % i == 0:
#             l.append(i)
#     return max(l)
#
# print(div_min_max(98985678))

# def sum_lists_elements(lista):
#     return lista[0]


# def no_boring_zeros(n):
#     return int(str(n).rstrip("0"))
#
# print(no_boring_zeros(165))

# from collections import Counter
#
# def count(s):
#     lista = list(Counter(s).values())
#     print(lista)
#     return [value for key, value in Counter(s).items()]


# from collections import Counter
#
# def count(inta):
#     return Counter(inta)
#
#
# print(count((1, 2, 3, 1, 'e')))

#
# def gsd_func(x, y):
#     if y == 0:
#         return x
#     else:
#         return gsd_func(y, x % y)
#
#
# assert gsd_func(54, 24) == 6, "Error"


def str_to_int(s, d):
    return map(lambda x, y: int(x) ** y, s, d)

print(list(str_to_int('1234567', [1, 2, 3, 4, 5, 6, 7])))
