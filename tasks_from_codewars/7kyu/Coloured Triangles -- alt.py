"""
Disclaimer
This Kata is an insane step-up from Avanta's Kata, so I recommend to solve it first before trying this one.

Problem Description
A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.

For example, different possibilities are:

Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
With a bigger example:

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
You will be given the first row of the triangle as a string and its your job to return the final colour which would
appear in the bottom row as a string. In the case of the example above, you would be given 'RRGBRGBB',
  and you should return 'G'.

Constraints
1 <= length(row) <= 10 ** 5

The input string will only contain the uppercase letters 'B', 'G' or 'R'.

The exact number of test cases will be as follows:

100 tests of 100 <= length(row) <= 1000
100 tests of 1000 <= length(row) <= 10000
100 tests of 10000 <= length(row) <= 100000
Examples
triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'

"""


def next_color(tr):
    if tr[0] != tr[1] and tr[0] != tr[2] and tr[1] != tr[2]:
        return tr[1]
    elif tr[0] == tr[1]:
        return tr[2]
    elif tr[1] == tr[2]:
        return tr[0]
    else:
        return "RGB".replace(tr[0], '').replace(tr[1], '')


def next_str(s):
    result = ""
    for n in range(0, len(s)-2):
        result += next_color(s[n: n+3])
    return result


def triangle(row):
    while len(row)-1:
        if len(row) == 2:
            return "RGB".replace(row[0], '').replace(row[1], '') if row[0] != row[1] else row[0]
        else:
            row = next_str(row)
    return row


print(triangle("RBRGBRBGGRRRBGBBBGG"))
