"""
DESCRIPTION:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(itr):
    ulist = []
    if type(iter) is not list:
        itr = list(itr)
    pr = ''
    for elm in itr:
        if pr != elm:
            pr = elm
            ulist.append(elm)
    return ulist


# i = ('AAAABBBCCDAABBB')
# i = ('ABBCcAD')
i = ([1, 2, 2, 3, 3, 2, 2, 2, 1, 1, ])

print(unique_in_order(i))
