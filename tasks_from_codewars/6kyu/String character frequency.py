"""
6kyu

In this Kata, we are going to determine if the count of each of the characters in a string can be equal if we remove a single character from that string.

For example:

solve('abba') = false -- if we remove any character, the count of each character will not be equal.
solve('abbba') = true -- if we remove one b, the count of each character becomes 2.
solve('aaaa') = true -- if we remove one character, the remaining characters have same count.
solve('wwwf') = true -- if we remove f, the remaining letters have same count.
More examples in the test cases. Empty string is not tested.

Good luck!
"""


from collections import Counter


def solve(s):
    l = list(Counter(s).values())
    return True if max(l) == min(l) == 1 or len(l) == 1 or sum(l) - 1 == max(l) * (len(l) - 1) else sum(l) - 1 == min(l) * len(l)


# print(solve("efghijklmnopqrst"))
print(solve("ooooon"))


"""
Best code:
from collections import Counter

def solve(s):
    return any(len(set(Counter(s.replace(c, '', 1)).values())) == 1 for c in s)
"""