"""
DESCRIPTION:
Hello. Today our job is to find the Nth Pipi number.

Let us define Pn such that the following expression:

P0+P1+P2+...Pn−1+PnP_{0}+\sqrt{P_{1}+\sqrt{P{_2}+\sqrt{...\sqrt{P_{n-1}+\sqrt{P_n}}}}}P
0
​
 +
P
1
​
 +
P
2
​
 +
...
P
n−1
​
 +
P
n
​

​

​

​

​

​


is equal to n, if P0 = 0.

Examples:
pipi(0) == 0
because

0=00 = 00=0

pipi(1) == 1
because

0+1=10+\sqrt{1} = 10+
1
​
 =1

pipi(2) == 9
because

0+1+9=20+\sqrt{1+\sqrt{9}} = 20+
1+
9
​

​
 =2

pipi(3) == 3025
because

0+1+9+3025=30+\sqrt{1+\sqrt{9+\sqrt{3025}}} = 30+
1+
9+
3025
​

​

​
 =3

Number N range:
From 0 to 21.

Note: 2000 characters restriction to prevent hard-coding.
"""

from functools import cache

@cache
def pipi(n):
    if n in [0, 1]:
        return n
    else:
        res = (n**2 - 1)**2
        for i in range(2, n):
            res = (res - pipi(i))**2
        return res


print(pipi(3))

"""
Best code:

from functools import lru_cache

@lru_cache()
def pipi(n):
    if n == 0:
        return n
    else:
        for i in range(n):
            n = (n - pipi(i))**2
        return n
        
"""