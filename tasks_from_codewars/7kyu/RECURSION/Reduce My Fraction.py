"""
Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

"""


import math

def reduce_fraction(arr):
    return tuple(map(lambda x: x // math.gcd(*arr), arr))


arr = (30,18)
print(reduce_fraction(arr))


"""
Best Practice:

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    
def reduce_fraction(fraction):
    num, denom = fraction
    gcd_num_denom = gcd(num, denom)
    return (num // gcd_num_denom, denom // gcd_num_denom)
    
"""