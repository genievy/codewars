"""
Convert string to camel case

DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    text = text.replace('-', '_').split('_')
    s = text[0]
    for i in text[1:]:
        s = s + i.title()
    return s

# # fine from codewars
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


text = "the-stealth_warrior"
print(to_camel_case(text))
