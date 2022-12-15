"""
Write a rotate function that rotates a two-dimensional array (a matrix) either clockwise or anti-clockwise by 90 degrees, and returns the rotated array.

The function accepts two parameters: an array, and a string specifying the direction or rotation. The direction will be either "clockwise" or "counter-clockwise".

Here is an example of how your function will be used:

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate(matrix, "clockwise") #  Would return  [[7, 4, 1], [8, 5, 2],  [9, 6, 3]]
To help you visualize the rotated matrix, here it is formatted as a grid:

 [[7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]]
Rotated counter-clockwise it would looks like this:

 [[3, 6, 9],
  [2, 5, 8],
  [1, 4, 7]]
"""


def rotate(matrix, direction):
    result = []
    if direction == "clockwise":
        rank = (0, len(matrix[0]))
        for i in range(*rank):
            l = [matrix[n][i] for n in range(0, len(matrix))]
            l.reverse()
            result.append(l)
        return result
    else:
        rank = (len(matrix[0])-1, -1, -1)
        for i in range(*rank):
            l = [matrix[n][i] for n in range(0, len(matrix))]
            result.append(l)
        return result


direction = 'clockwise'
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]

print(rotate(matrix, direction))

"""
Best Code:

def rotate(matrix, direction): 
    return [list(i)[::-1] for i in zip(*matrix)] if direction == "clockwise" else [list(i) for i in reversed(list(zip(*matrix)))]
    

or

def rotate(matrix, direction): 
    if direction == 'clockwise':
        return [[row[i] for row in reversed(matrix)] for i in range(len(matrix[0]))]
    return [[row[i] for row in matrix] for i in reversed(range(len(matrix[0])))]
    
"""