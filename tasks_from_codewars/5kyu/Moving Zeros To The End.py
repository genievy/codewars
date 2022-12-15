"""
Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

Example:
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

def move_zeros(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] != 0] + [0] * lst.count(0)


lst = [1, 0, 1, 2, 0, 1, 3]
print(move_zeros(lst))


# good code:
# def move_zeros(lst):
#     return [x for x in lst if x] + [0]*lst.count(0)