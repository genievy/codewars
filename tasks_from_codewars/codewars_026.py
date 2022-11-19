"""
Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance.
For empty output return (an empty list).

Consult the solution set-up for the exact data structure implementation depending on your language.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
"""


# def ordered_count(inp):
#     def count(inp, i):
#         return (i, inp.count(i))
#     [count(inp, n) for n in inp]

# [l.append((n, inp.count(n))) for n in inp if ]


def ordered_count(inp):
    l = []
    for n in inp:
        if (n, inp.count(n)) not in l:
            l.append((n, inp.count(n)))
    return l


inp = "nlkugiluhpouywo8eyrp hv wg vcyewqgirdyqb"

print(ordered_count(inp))
