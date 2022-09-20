"""
Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(string):
    dicta = {}
    for i in string:
        if i in dicta.keys():
            dicta[i] += 1
        else:
            dicta[i] = 1
    return dicta


string = 'bananarama'
print(count(string))

# Best code
# def count(string):
#     return {i: string.count(i) for i in string}