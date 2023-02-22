"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    sorted_only_odd_array = sorted([i for i in source_array if i % 2])
    return list(sorted_only_odd_array.pop(0) if val % 2 else val for val in source_array)

print(sort_array([5, 3, 2, 8, 1, 4]))