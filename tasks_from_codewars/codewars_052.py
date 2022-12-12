
def sort_my_string(s):
    a = [char for x, char in enumerate(stra) if not x % 2]
    b = [" "] + [char for x, char in enumerate(stra) if x % 2]
    a.extend(b)
    return "".join(a)


stra = "CodeWars"
print(sort_my_string(stra))


"""
Best Code:

def sort_my_string(s):
    return '{} {}'.format(s[::2], s[1::2])
    
"""
