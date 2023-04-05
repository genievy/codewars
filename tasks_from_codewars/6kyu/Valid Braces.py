def valid_braces(string):
    l1 = ['(', '[', '{']
    l2 = [')', ']', '}']
    for num, val in enumerate(string):
        print(string[num + 1])
        print(l2.index(string[num + 1]))
        print(l1.index(string[num]))
        if val in l1 and string[num + 1] in l2 or val in l2 and string[num + 1] in l1 or l2.index(string[num + 1]) == l1.index(string[num]):
            return True
        return False


print(valid_braces("{}(){[]}"))
