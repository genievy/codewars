"""
Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.

This should only work if the number has 4 digits or more. If not, return "Number is too small".

Example
lowest_product("123456789") --> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
"""


def lowest_product(input, out="Number is too small"):
    if len(input) > 3:
        out = min([int(input[n])*int(input[n+1])*int(input[n+2])*int(input[n+3]) for n in range(0, len(input) - 3)])
    return out
