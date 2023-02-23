"""
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
"""

def tower_builder(n_floors):
    res = []
    for i in range(n_floors):
        res.append(("*" + "*" * i * 2).center((2*n_floors - 1), " "))
    return res


