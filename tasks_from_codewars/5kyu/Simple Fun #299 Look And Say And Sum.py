"""
Task
Get the digits sum of nth number from the Look-and-Say sequence(1-based).

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

Input/Output
[input] integer n

nth number in the sequence to get where 1 <= n <= 55 and n=1 is "1".

[output] an integer

The sum of digits in nth number from the Look-and-Say sequence.

Example
For n = 2, the output shoule be 2.

"11" --> 1 + 1 --> 2

For n = 3, the output shoule be 3.

"21" --> 2 + 1 --> 3

For n = 4, the output shoule be 5.

"1211" --> 1 + 2 + 1 + 1 --> 5
"""

import itertools

def look_and_say_and_sum(n):
    x = "1"
    for i in range(n-1):
        # Applying the algorithm by Nicola Vanoni, Web Developer from Mantova, Italy
        x = ''.join(str(len(list(g)))+k for k, g in itertools.groupby(x))
    return sum(map(lambda i: int(i), x))

print(look_and_say_and_sum(55))


# """
# Also my code, but slower:
# """
# def number(s):
#     result = ''
#     while s:
#         s1 = s.replace(s.lstrip(s[0]), '')
#         result += f'{len(s1)}{s1[0]}'
#         s = s.lstrip(s1)
#     return result
#
# def look_and_say_and_sum(n):
#     numb = '1'
#     while n - 1:
#         numb = number(numb)
#         n -= 1
#     return sum(map(lambda x: int(x), numb))
