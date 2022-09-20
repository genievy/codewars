

def same(l1, l2):
    li = []
    for i in range(0, len(l1)):
        if l1[i].isalpha() and l2[i].isalpha():
            if  l1[i].isupper() and l2[i].isupper() or l1[i].islower() and l2[i].islower():
                li.append(1)
            else:
                li.append(0)
        else:
            li.append(-1)
    return li


l1 = 'QedhgrtRt'
l2 = 'JKLl;l9kj'


print(same(l1, l2))
