

class IncrementCounter:

    def __init__(self):
        self._value = 0

    def new_value(self):
        self._value += 1
        return self._value

    def reset(self):
        self._value = 0
        return self._value

counter1 = IncrementCounter()
counter2 = IncrementCounter()

class Count:
    def __init__(self, v):
        pass

    def divisors(self, v):
        self.v = v
        counter1.reset()
        for i in range(2, v):
            if self.v % i == 0:
                counter1.new_value()
        return counter1.new_value()

tipo = Count(0)


# на 12.06 оптимальный код t = 6.041 seconds
def count_pairs_int(diff, n_max):
    c = 0
    for i in range(2, n_max, diff):
        list2 = [len([i for i in range(2, n) if not n % i]) for n in range(i, i + diff)]
        for n in range(diff):
            try:
                if all(map(lambda a, b: list1[n] == list2[n], list1, list2)):
                    c += 1
            except:
                continue
        list1 = list2
    return c

n_max = 350
diff = 6
print(count_pairs_int(diff, n_max))
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
