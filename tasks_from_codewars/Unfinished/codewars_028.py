

# def find_dups_miss(arr):
#     double_num = []
#     for i in arr:
#         if arr.count(i) - 1 and i not in double_num:
#             double_num.append(i)
#     double_num.sort()
#     for n in range(min(arr), max(arr)):
#         if n not in arr:
#             break
#     return [n, double_num]


def find_dups_miss(arr):
    global absent
    arr.sort()
    double_num = []
    for i in range(min(arr), max(arr)):
        if not arr.count(i) - 2:
            double_num.append(i)
        elif not arr.count(i):
            absent = i
    return [absent, double_num]


arr = [10,9,8,9,6,1,2,4,3,2,5,5,3]
print(find_dups_miss(arr))  # == [7,[2,3,5,9]]
