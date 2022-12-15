"""
This is a question from codingbat

Given an integer n greater than or equal to 0, create and return an array with the following pattern:

squareUp(3) => [0, 0, 1, 0, 2, 1, 3, 2, 1]
squareUp(2) => [0, 1, 2, 1]
squareUp(4) => [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
"""


def square_up(n):
    result, l = [], [0] * n
    for k in range(n):
        l[n - k - 1] = k + 1
        result.extend(l)
    return result


print(square_up(9))
