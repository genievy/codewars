"""
Given an array (or list) of scores, return the array of ranks for each value in the array. The largest value has rank 1, the second largest value has rank 2, and so on. Ties should be handled by assigning the same rank to all tied values. For example:

ranks([9,3,6,10]) = [2,4,3,1]
and

ranks([3,3,3,3,3,5,1]) = [2,2,2,2,2,1,7]
because there is one 1st place value, a five-way tie for 2nd place, and one in 7th place.
"""

# def ranks(arr):
#     result, n, m = [0] * len(arr), 1, 1
#     while arr != [0] * len(arr):
#         n = m = m
#         for i in range(len(arr)):
#             if arr[i] == max(arr):
#                 if arr[i] in arr[i + 1:]:
#                     result[i], arr[i] = n, 0
#                     m += 1
#                 else:
#                     result[i], arr[i] = n, 0
#                     m += 1
#                     break
#     return result


def ranks(a):
    arr = []
    arr.extend(a)
    m = 1
    l = len(arr)
    if l:
        minimum = min(arr) - 1
    else:
        minimum = 0
    result = [minimum] * l
    while m <= l:
        n = m
        for i in range(len(arr)):
            maximus = max(arr)
            if arr[i] == maximus:
                if arr[i] in arr[i + 1:]:
                    result[i], arr[i] = n, minimum
                    m += 1
                else:
                    result[i], arr[i] = n, minimum
                    m += 1
                    break
    return result


# print(ranks([3, 3, 7, 3, 3, 5, 1]))
print(ranks([-27, 98, 35, 19, -71, 98, -23, -49, 87, -70, -15, 10, -11, 88, 79, -67, -23, 22, 58, -66, 49, 7]))
# Best codes:
#
# def ranks(a):
#   sortA = sorted(a, reverse=True)
#   return [sortA.index(s) + 1 for s in a]
#
#
# def ranks(a):
#     return [sorted(a, reverse = True).index(m) + 1 for m in a]
#
#
# def ranks(a):
# 	dict = {v: k for k, v in sorted(enumerate(sorted(a, reverse=True), start=1), reverse=True)}
# 	return [dict[i] for i in a]
