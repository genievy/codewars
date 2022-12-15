"""
Calculating with Functions

This time we want to write calculations using functions and get the results. Let's have a look at some examples:
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
"""


def zero(a=None):
    if a:
        return a[0](0, a[1])
    else:
        return 0


def one(a=None):
    if a:
        return a[0](1, a[1])
    else:
        return 1


def two(a=None):
    if a:
        return a[0](2, a[1])
    else:
        return 2


def three(a=None):
    if a:
        return a[0](3, a[1])
    else:
        return 3


def four(a=None):
    if a:
        return a[0](4, a[1])
    else:
        return 4


def five(a=None):
    if a:
        return a[0](5, a[1])
    else:
        return 5


def six(a=None):
    if a:
        return a[0](6, a[1])
    else:
        return 6


def seven(a=None):
    if a:
        return a[0](7, a[1])
    else:
        return 7


def eight(a=None):
    if a:
        return a[0](8, a[1])
    else:
        return 8


def nine(a=None):
    if a:
        return a[0](9, a[1])
    else:
        return 9


def plus(*b):
    argument = locals().get('b')[0]

    def inner(*d):
        return d[0] + d[1]
    return inner, argument


def minus(*b):
    argument = locals().get('b')[0]

    def inner(*d):
        return d[0] - d[1]
    return inner, argument


def times(*b):
    argument = locals().get('b')[0]

    def inner(*d):
        return d[0] * d[1]
    return inner, argument


def divided_by(*b):
    argument = locals().get('b')[0]

    def inner(*d):
        return d[0]//d[1]
    return inner, argument



print(nine(divided_by(three())))
# print(seven(times(five())))

# Best code

# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)
#
# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y
