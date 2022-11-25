"""
Given a standard english sentence passed in as a string, write a method that will return a sentence made up of the same
words, but sorted by their first letter. However, the method of sorting has a twist to it:

All words that begin with a lower case letter should be at the beginning of the sorted sentence, and sorted in ascending
order.
All words that begin with an upper case letter should come after that, and should be sorted in descending order.
If a word appears multiple times in the sentence, it should be returned multiple times in the sorted sentence.
Any punctuation must be discarded.

Example
For example, given the input string "Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!",
your method should return "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut".
Lower case letters are sorted a -> l -> l -> o -> o -> t and upper case letters are sorted V -> T -> O -> M -> L -> C.
"""


def pseudo_sort(st):
    s, l, l_2 = '', [], []
    for i in st:
        if i.isalpha() or i.isspace():
            s += i
    for i in s.split(' '):
        if i[0].istitle():
            l_2.append(i)
        else:
            l.append(i)
    l.sort()
    l_2.sort(reverse=True)
    l.extend(l_2)
    return " ".join(l)

s = "Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"

print(pseudo_sort(s))