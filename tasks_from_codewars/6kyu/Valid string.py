"""
Test if the string can be entirely formed by consecutively concatenating words of the dictionary.

For example:

dictionary: ["code", "wars"]

s1:         "codewars" =>  true  -> match 'code', 'wars'
s2:         "codewar"  =>  false -> match 'code', unmatched 'war'
One word from the dictionary can be used several times.
"""


def valid_word(seq, word: str, result=False):
    for i in range(len(seq)):
        word_prim = word
        li = seq[i:] + seq[:i]
        for a in range(len(word)):
            for n in li:
                if word_prim.startswith(n):
                    word_prim = word_prim.replace(n, '', 1)
                    break
            if len(word_prim) == 0:
                result = True
                break
        if result:
            break
    return result


print(valid_word(['psfp', 'zkuko', 'ifouzkuko', 'eaif', 'ea', 'loo', 'psf'], 'psfpsfeaifouzkukoealoo'))
# print(valid_word(['ab', 'bc'], 'abc'))
# print(valid_word(['ab', 'a', 'bc'], 'abc'))
# print(valid_word(['a', 'b', 'c', 'd', 'e', 'f'], 'abcdefg'))
# print(valid_word(['gb', 'opzn', 'gbg', 'gb', 'pzn', 'bji', 'zgb', 'o', 'pzn', 'gbqgq', 'qgqd'] , 'gbbjipznoopznzgbgbgbqgqdpzn'))
