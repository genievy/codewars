"""
Write a method named getExponent(n,p) that returns the largest integer exponent x such that px evenly divides n.
if p<=1 the method should return null/None (throw an ArgumentOutOfRange exception in C#).
"""


def get_exponent(n, p=None):
    if p > 1:
        l, x = [], 0
        while abs(n) // (p ** x) >= 1:
            if n % (p ** x) == 0:
                l.append(x)
                x += 1
            else:
                x += 1
        else:
            return max(l)


a = -250
b = 5
print(get_exponent(a, b))


"""
Best Practices

def get_exponent(n, p):
    if p > 1:
        x = 0
        while not n % p:
            x += 1
            n //= p
        return x
        
and

def get_exponent(n, p, i = 0):
    if p <= 1: return None
    return get_exponent(n / p, p, i + 1) if n / p == n // p else i
          
"""
