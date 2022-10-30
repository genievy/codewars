# class IncrementCounter:
#
#     def __init__(self):
#         self._value = 0
#
#     def new_value(self):
#         self._value += 1
#         return self._value
#
#     def reset(self):
#         self._value = 0
#         return self._value
#
#
# def divisors(n):
#     counter = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             counter += 1
#     return counter
#
#
# def count_pairs_int(diff, n_max):
#     li =[divisors(i) for i in range(1, n_max+1)]
#     for k in range(0, diff):
#         for g in range(0, len(li) - diff, diff):
#             try:
#                 if li[k+g] == li[k+g+diff]:
#                     counter1.new_value()
#             except:
#                 continue
#     return counter1.new_value()-1

########################################################


# def count_pairs_int(diff, n_max):
#     def div(n):
#         return len([i for i in range(2 , n) if n % i == 0])
#     c = 0
#     for n in range(2,  n_max-diff):
#         if div(n) == div(n + diff):
#             c += 1
#     return c

########################################################




#########################################################


# counter1 = IncrementCounter()
# diff = 6
# n_max = 10000
#
# print(count_pairs_int(diff, n_max))


###############################################################
# # Проверка, является ли число числом Фибоначчи
#
# #fib = lambda n: True if sqrt(5*(n**2)-4)%1 == 0 or sqrt(5*(n**2)+4)%1 == 0 else False
#
#
# def fib(n):
#     return True if sqrt(5*(n**2)-4)%1 == 0 or sqrt(5*(n**2)+4)%1 == 0 else False
#
#
# digit = 5
# print(fib(digit))


############################################################################


# def list_prod():
#     list_prod = [f(n)^2 + f(n)*f(n+1) for n in ]

# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+ b
#
#
# f = fib()
# for x in range(numbers_fib):
#     print(next(f))


# from math import log
#
#
# def fibinv(f):
#     if f < 2:
#         return f
#     return int(round(log(f * 5**0.5) / log(phi)))
#

# phi = (1 + 5**0.5) / 2
# # Возвращает число Фиббоначчи ряда (n)
# def fib(n):
#     return int(round((phi**n - (1-phi)**n) / 5**0.5))

def int32_to_ip(inta):
    s = bin(inta)[2::] # stroka chisel
    a = s.zfill(32) # stroka, dopolnennaja sleva nulyami
    l = [int(a[2+n: 10+n: 1], 2) for n in range(0, 25, 8)]
    return '.'.join(l)