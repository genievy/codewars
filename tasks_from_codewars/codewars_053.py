"""
Welcome
This kata is inspired by This Kata

We have a string s

We have a number n

Here is a function that takes your string, concatenates the even-indexed chars to the front, odd-indexed chars
to the back.

Examples
s = "Wow Example!"
result = "WwEapeo xml!"
s = "I'm JomoPipi"
result = "ImJm ii' ooPp"
The Task:
return the result of the string after applying the function to it n times.

example where s = "qwertyuio" and n = 2:

after 1 iteration  s = "qetuowryi"
after 2 iterations s = "qtorieuwy"
return "qtorieuwy"
Note
there's a lot of tests, big strings, and n is greater than a billion

so be ready to optimize.

"""


def jumbled_string(s, n):
    s1 = s
    n1 = n
    while n:
        if s == s1 and n != n1:
            n = n1 % (n1 - n)
            n1 = n
        else:
            s = s[::2] + s[1::2]
            n = n - 1
    return s


print(jumbled_string("1234567890123456789qwerty", 34))

"""
Best code:

def jumbled_string(s, n):
    iterations = [s]
    
    while True:
        s = s[::2] + s[1::2]
        if s == iterations[0]: break
        iterations.append(s)
    
    return iterations[n % len(iterations)]
    
"""





# stra = "1234567890"
# stra1 = "1234567890"
# n = 50
# n1 = 50
# print(jumbled_string(stra, stra1, n, n1))
# print(jumbled_string("1234567890", 34))

