"""
Linked Lists - Remove Duplicates

Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes
from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined.

Remember to return the head of the list.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):

    def len_of_data(h):
        if isinstance(h.data, int):
            return 1
        else:
            return len(h.data)

    if not head:
        return head
    elif len_of_data(head) == 1:
        return head

    head_result = []
    for i in range(1, len_of_data(head)):
        if head.data[i] != head.data[i - 1]:
            head_result.append(head.data[i - 1])
    return head_result



    # else:
    #     return [head.data.remove(i) for i in range(6) if head.data[-1] == head.data[-2]]


data = [1, 2, 3, 3, 4, 4, 5]
build_list = Node
# print(remove_duplicates(build_one_two_three()))
print(remove_duplicates(build_list(data)))
