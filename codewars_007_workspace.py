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

##############################################################

# # # на 12.06 оптимальный код t = 6.041 seconds
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


##############################################################

# Тоже быстрый код t = 6.891 seconds
# def divisors(n):
#     counter = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             counter += 1
#     return counter


def count_pairs_int(diff, n_max):
    def divisors(n):
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1
        return counter
    li =[divisors(i) for i in range(1, n_max+1)]
    for k in range(0, diff):
        for g in range(0, len(li) - diff, diff):
            try:
                if li[k+g] == li[k+g+diff]:
                    counter1.new_value()
            except:
                continue
    return counter1.new_value()-1


################################################################

# class Count:
#     def __init__(self):
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
# tipo = Count()
#
# def count_pairs_int(diff, n_max):
#     li_full = []
#     for i in range(0, diff):
#         li = [tipo.divisors(k + i) for k in range(2, n_max-diff, diff)]
#         li_full.append(li)
#     for m in range(len(li_full)-1):
#         for d in range(len(li)):
#             if li_full[m][d] == li_full[m + 1][d]:
#                 counter2.new_value()
#     f = counter2.new_value()
#     return f

##############################################################


n_max = 10000
diff = 6
print(count_pairs_int(diff, n_max))
