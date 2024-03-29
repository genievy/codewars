"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
"""


def digitize(n):
    return [int(i) for i in str(n)[::-1]]


"""
Best practice:

def digitize(n):
    return map(int, str(n)[::-1])
    
"""

n = 35231
print(digitize(n))
