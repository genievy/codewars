"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)
"""

# I like it!

def find_missing_letter(chars:list):
    sum_ascii_reducced = sum(map(ord, chars))
    sum_ascii_end2end = sum(range(ord(chars[0]), ord(chars[-1])+1))
    return chr(sum_ascii_end2end - sum_ascii_reducced)