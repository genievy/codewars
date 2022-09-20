"""
Split Strings

DESCRIPTION:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s):
    d = []
    for i in range(0, len(s), 2):
        try:
            d.append(s[i] + s[i+1])
        except:
            d.append(s[i] + "_")
    return d
