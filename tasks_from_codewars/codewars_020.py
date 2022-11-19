"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
Best code
"""


def pig_it(text):
    list = []
    for v in text.split():
        if v.isalpha():
            list.append(v[1::] + v[0] + 'ay')
        else:
            list.append(v)
    return ' '.join(list)


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
#