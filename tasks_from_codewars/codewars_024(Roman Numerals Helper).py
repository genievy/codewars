"""
    Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
    Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000
In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""


class RomanNumerals:
    def __init__(self, val):
        self.lrom = ['M', 'D', 'C', 'L', 'LX',  'X', 'V', 'IV', 'I']
        self.lara = [1000, 500, 100, 50, 10, 5, 4, 1]
        self.lres = []
        self.val = val

    def to_roman(self):
        for n in range(0, len(self.lara)):
            x = self.val // self.lara[n]
            if x:
                self.lres.append(self.lrom[n] * x)
                print(x)
                print(self.lrom[n])
                self.val -= self.lara[n] * x
                print(self.val)
            else:
                continue
        return self.lres

    # def from_roman(roman_num):
    #     return 0

print(RomanNumerals(1985).to_roman())
