"""
Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of aba^ba
b
 . Note that aaa and bbb may be very large!

For example, the last decimal digit of 979^79
7
  is 999, since 97=47829699^7 = 47829699
7
 =4782969. The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2
200
 )
2
300

 , which has over 109210^{92}10
92
  decimal digits, is 666. Also, please take 000^00
0
  to be 111.

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""


def last_digit(n1, n2):
    if not n1 % 10 and n2:
        return 0
    else:
        return ((n1 % 100) ** (n2 % 100)) % 10


print(last_digit(19572112970995074255718649295554002899114938448244727577542, 7186585254290472478242086687636808768844747028176531))
