"""
DESCRIPTION:
The integers 14 and 15, are contiguous (1 the difference between them, obvious) and have the same number of divisors.

14 ----> 1, 2, 7, 14 (4 divisors)
15 ----> 1, 3, 5, 15 (4 divisors)
The next pair of contiguous integers with this property is 21 and 22.

21 -----> 1, 3, 7, 21 (4 divisors)
22 -----> 1, 2, 11, 22 (4 divisors)
We have 8 pairs of integers below 50 having this property, they are:

[[2, 3], [14, 15], [21, 22], [26, 27], [33, 34], [34, 35], [38, 39], [44, 45]]
Let's see now the integers that have a difference of 3 between them. There are seven pairs below 100:

[[2, 5], [35, 38], [55, 58], [62, 65], [74, 77], [82, 85], [91, 94]]
Let's name, diff, the difference between two integers, next and prev, (diff = next - prev) and nMax, an upper bound of the range.

We need a special function, count_pairsInt(), that receives two arguments, diff and nMax and outputs the amount of pairs of integers that fulfill this property, all of them being smaller (not smaller or equal) than nMax.

Let's see it more clearly with examples.

count_pairsInt(1, 50) -----> 8 (See case above)
count_pairsInt(3, 100) -----> 7 (See case above)
Happy coding!!!
"""


from math import sqrt

def count_pairs_int(diff, n_max):
    def div(n):
        """
        The div function uses iteration to the root of a number
         to find its divisors instead of iterating to the number itself.
         This speeds up code execution
        """
        count = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count

    c = 0
    for n in range(1, n_max - diff):
        if div(n) == div(n + diff):
            c += 1
    return c

n_max = 150000
diff = 6
print(count_pairs_int(diff, n_max))


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
# counter1 = IncrementCounter()
# counter2 = IncrementCounter()
#
# class Count:
#     def __init__(self, v):
#         pass
#
#     def divisors(self, v):
#         self.v = v
#         counter1.reset()
#         for i in range(2, v):
#             if self.v % i == 0:
#                 counter1.new_value()
#         return counter1.new_value()
#
# tipo = Count(0)
#
#
# # на 12.06 оптимальный код t = 6.041 seconds
# def count_pairs_int(diff, n_max):
#     c = 0
#     for i in range(2, n_max, diff):
#         list2 = [len([i for i in range(2, n) if not n % i]) for n in range(i, i + diff)]
#         for n in range(diff):
#             try:
#                 if all(map(lambda a, b: list1[n] == list2[n], list1, list2)):
#                     c += 1
#             except:
#                 continue
#         list1 = list2
#     return c
#
# n_max = 350
# diff = 6
# print(count_pairs_int(diff, n_max))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# лучшее решение через класс, а счетчик внутри ф-ции
# class Count:
#     def __init__(self, diff, n_max):
#         self.diff = diff
#         self.n_max = n_max
#
#     def  count_pairs_int(self):
#         c = 0
#         for i in range(2, self.n_max, self.diff):
#             list2 = [len([i for i in range(2, n) if not n % i]) for n in range(i, i + self.diff)]
#             for n in range(self.diff):
#                 try:
#                     if all(map(lambda a, b: list1[n] == list2[n], list1, list2)):
#                         c += 1
#                 except:
#                     continue
#             list1 = list2
#         return c
#
# p1 = Count(6, 350)
# print(p1.count_pairs_int())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # решения через класс co счетчиком
# def count_pairs_int(diff, n_max):
#     counter2.reset()
#     def div(v):
#         counter1.reset()
#         for i in range(2, v):
#             if v%i == 0:
#                 counter1.new_value()
#         return counter1.new_value()
#     for n in range(2, n_max-diff):
#         if div(n) == div(n + diff):
#             counter2.new_value()
#     return counter2.new_value() - 1
#
# n_max = 350
# diff = 6
# print(count_pairs_int(diff, n_max))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# c применением класса вариант_1
# def count_pairs_int(diff, n_max):
#     def div(v):
#         counter1.reset()
#         for i in range(2, v):
#             if v%i == 0:
#                 counter1.new_value()
#         return counter1.new_value()
#     for i in range(2, n_max, diff):
#         list2 = [div(n) for n in range(i, i + diff)]
#         for n in range(diff):
#             try:
#                 if all(map(lambda a, b: list1[n] == list2[n], list1, list2)):
#                      c = counter2.new_value()
#             except:
#                 continue
#         list1 = list2
#     return c
#
# n_max = 350
# diff = 6
# print(count_pairs_int(diff, n_max))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# integer = 12
# tipo.divisors(integer)
# p1 = Count(6, 350)
# print(p1.count_pairs_int())


# def count_pairs_int(diff, n_max):
#     c = 0
#     primes = []
#     for i in range(2, n_max + 1):
#         if all(i % j != 0 for j in primes):
#             primes.append(i)
#     for i in range(2, n_max, diff):
#         list2 = [len([p for p in primes if n % p == 0]) for n in range(i, i + diff)]
#         if all(map(lambda a, b: list1[n] == list2[n], list1, list2)):
#             c += 1
#         list1 = list2
#     return c



##############################################################

# Ускорено через мемоизацию.

# def count_pairs_int(diff, n_max):
#     def div(n, memo={}):
#         if n in memo:
#             return memo[n]
#         memo[n] = len([i for i in range(2 , n) if n % i == 0])
#         return memo[n]
#
#     c = 0
#     for n in range(2,  n_max-diff):
#         if div(n) == div(n + diff):
#             c += 1
#     return c

# Ускорение за счет уменьшения вызовов ф-ции div:

# def count_pairs_int(diff, n_max):
#     def div(n):
#         count = 0
#         for i in range(2, n):
#             if n % i == 0:
#                 count += 1
#         return count
#     c = 0
#     for n in range(2, n_max-diff):
#         if div(n) == div(n + diff):
#             c += 1
#     return c

# # Мой код:
#
# def count_pairs_int(diff, n_max):
#     def div(n):
#         return len([i for i in range(2 , n) if n % i == 0])
#     c = 0
#     for n in range(2,  n_max-diff):
#         if div(n) == div(n + diff):
#             c += 1
#     return c
