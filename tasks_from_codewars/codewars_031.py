"""
For example:

 Given arr = [1,-2,3,4,-5,-4,3,2,1],
       range = [[1,3],[0,4],[6,8]]
 should return 6

 calculation process:
 range[1,3] = arr[1]+arr[2]+arr[3] = 5
 range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
 range[6,8] = arr[6]+arr[7]+arr[8] = 6
 So the maximum sum value is 6
Note:
arr/$a always has at least 5 elements;
range/$range/ranges always has at least 1 element;
All inputs are valid;
This is a simple version, if you want some challenge, please try the challenge version.
Some Examples
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3],[0,4],[6,8]]) === 6
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3]]) === 5
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,4],[2,5]]) === 0
"""


def max_sum(arr, ranges):
    range_list = []
    for l in ranges:
        result = 0
        for i in range(l[0], l[1]+1):
            result += arr[i]
        range_list.append(result)
    print(range_list)
    return max(range_list)



arr = [1,-2,3,4,-5,-4,3,2,1]
ranges = [[1,3],[0,4],[6,8]]

print(max_sum(arr, ranges))
