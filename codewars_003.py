"""
Square Every Digit

DESCRIPTION:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""

# def square_digits(num):
#     s = []
#     for index in list(str(num)):
#         s.append(int(index)**2)
#     return int(''.join([str(i) for i in s]))
#

# def square_digits(num):
#     s = []
#     [s.append(int(i)**2) for i in str(num)]
#     return int(''.join([str(i) for i in s]))




# # fine code (not mine)
# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
        # print(int(ret))
    return int(ret)

num = 12351
print(square_digits(num))
