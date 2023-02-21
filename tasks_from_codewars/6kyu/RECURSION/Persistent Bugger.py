import functools


def persistence(n, count=0):
    if len(str(n)) == 1:
        return count
    else:
        lst = [int(i) for i in str(n)]
        return persistence(functools.reduce(lambda a, b: a * b, lst), count+1)


print(persistence(999))
