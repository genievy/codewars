"""
Product of consecutive Fib numbers

DESCRIPTION:
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true],
productFib(800) # should return [34, 55, false],
-----
productFib(714) # should return {21, 34, 1},
productFib(800) # should return {34, 55, 0},
-----
productFib(714) # should return {21, 34, true},
productFib(800) # should return {34, 55, false},
"""

# from math import log
#
#
# def productFib(prod):
#     """
#     Определяем n - ряд числа Фибоначчи (исходя из значения prod),
#     до которого будем генерировать произведение двух соседних чисел для сравнения этого произведения с prod:
#
#     1) prod = F(n) * F(n + 1)
#         известно, что F(n + 1) / F(n) = phi ==> F(n + 1) = phi * F(n),
#             где phi - т. н. "золотое сечение", которое определяется по формуле:
#             phi = (1 + 5 ** 0.5) / 2  .
#
#         т. о. prod = phi * F(n) ** 2, а
#         F(n) = (prod * phi) ** 0.5
#
#     2) Согласно формуле Бине число Фибоначи ряда n определяется как
#         F(n) = (phi ** n - (1 - phi) ** n) / 5 ** 0.5
#         Из-за ошибок округления с плавающей запятой это, однако, даст  правильный результат только для n < 70.
#         Поэтому к результату  функции, которая будет "инвертировать" формулу Брина и возвращать номер ряда
#         соответствующего числа Фибоначчи,  прибавим 1 :
#         n = int(round(log((((prod + 1) * phi) ** 0.5) * 5 ** 0.5) / log(phi))) + 1
#         также увеличим аргумент для log() на 1, чтобы избежать математической ошибки, если prod = 0
#
#     Далее создаем функцию генератора двух соседних чисел Фибоначчи с возрастанием
#
#     В цикле for сравниваем произведение двух чисел, которые возвращает генератор, с prod,
#     возвращая соответствующий массив
#     """
#     phi = (1 + 5 ** 0.5) / 2
#     base_fib = ((prod + 1) * phi) ** 0.5
#     n = int(round(log(base_fib * 5 ** 0.5) / log(phi))) + 1
#
#     def fibonacci(m):
#         a, b = 0, 1
#         for i in range(m):
#             yield a, b
#             a, b = b, a + b
#
#     for fib in fibonacci(n):
#         if fib[0] * fib[1] == prod:
#             return [fib[0], fib[1], True]
#         elif fib[0] * fib[1] > prod:
#             return [fib[0], fib[1], False]


def productFib(prod):
    a, b = 0, 1
    while a * b <= prod:
        if a * b == prod:
            return [a, b, True]
        a, b = b, a + b
        if a * b > prod:
            return [a, b, False]




prod = 210397365109278050825
print(productFib(prod))
