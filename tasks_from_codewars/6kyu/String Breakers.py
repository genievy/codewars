"""
I will give you an integer (N) and a string. Break the string up into as many substrings of N as you can without spaces. If there are leftover characters, include those as well.

Example:

n = 5;

st = "This is an example string";

Return value:
Thisi
sanex
ample
strin
g

Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'
"""

def string_breakers(n, st):
    st_united = st.replace(' ', '')
    l = []
    for i in range(0, len(st)//n +1):
        print(len(st)//n)
        l.append(st_united[n*i:n*(i+1)])
    st_new = '\n'.join(l)
    return st_new.strip('\n')


# st = "This is an example stringwwetyeyew"
# st = '4rutyhug1i0gz72in0kdxx7da900il1'
st = '7njeakx09k26f1ydk5lshkslkd1bbah5lhonut'
n = 20
print(string_breakers(n, st))
