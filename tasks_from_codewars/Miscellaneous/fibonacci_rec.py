

# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# from functools import lru_cache
#
# @lru_cache()
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)


# import decimal
#
#
# def fibonacci(n):
#     decimal.getcontext().prec = 10000
#
#     root_5 = decimal.Decimal(5).sqrt()
#     phi = ((1 + root_5) / 2)
#
#     a = ((phi ** n) - ((-phi) ** -n)) / root_5
#
#     return round(a)

"""
Для понимания меморизации

def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

или:

memoize = {0:0,1:1}
def fibonacci(n):
    if n not in memoize:
        memoize[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memoize[n]


Максимально быстрый:
"""

# from functools import cache
#
#
# @cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
