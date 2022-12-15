"""
Task:
Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands.
Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each
tile being a perfect 1 x 1piece of land. Some examples for better visualization:

['XOOXO',
  'XOOXO',
  'OOOXO',
  'XXOXO',
  'OXOOO']

should return: "Total land perimeter: 24",

while

['XOOO',
  'XOXO',
  'XOXO',
  'OOXX',
  'OOOO']

should return: "Total land perimeter: 18"

Good luck!
"""

def land_perimeter(arr):
    count = 0
    arr_b = arr + ["O" * len(arr[0])]
    for i in arr:
        d = "O"
        for n in i + "O":
            if n != d:
                count += 1
                d = n
    for n in range(len(arr_b[0])):
        d = "O"
        for i in arr_b:
            if i[n] != d:
                count += 1
                d = i[n]
    return count


arr = ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]
print(land_perimeter(arr))
