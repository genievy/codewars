"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

from operator import itemgetter


def order(sentence: str):

    def compare(snc):
        for i in snc:
            if i.isdigit():
                return i

    return ' '.join(sorted(sentence.split(), key=lambda x: compare(x)))


# def order(sentence:str):
#     lsn = sentence.split()
#     num = 0
#     for n in sentence:
#         if n.isdigit():
#             lsn[int(n)-1] = sentence.split()[num]
#             num += 1
#     return ' '.join(lsn) if sentence else sentence

print(order("4of Fo1r pe6ople g3ood th5e the2"))

"""
Best Practices:

def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))
"""

