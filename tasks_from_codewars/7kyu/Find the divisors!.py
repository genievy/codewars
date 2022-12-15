"""
Find the divisors!

DESCRIPTION:
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""


def divisors(integer):
    d = [i for i in range(2, integer) if integer % i == 0]
    return f'{integer} is prime' if len(d) == 0 else d


i = 556
print(divisors(i))


## fine code 1
# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l


## fine code 2
# def divisors(n):
    # return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n


class IncrementCounter:

    def __init__(self):
        self._value = 0

    def new_value(self):
        self._value += 1
        return self._value


counter1 = IncrementCounter()


# def div(n):
#     print([counter1.new_value() for i in range(2,n) if n%i == 0])
#     return [counter1.new_value() for i in range(2,n) if n%i == 0]

def div(n):
    for i in range(2,n):
        if n%i == 0:
            counter1.new_value()
    return counter1.new_value()


print(div(556))
