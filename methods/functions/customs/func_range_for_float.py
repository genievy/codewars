

def frange(start, stop, step):
    i = start
    while i < stop:
        yield round(i, 2)
        i += step


for i in frange(0.5, 1, 0.1):
    print(i)
