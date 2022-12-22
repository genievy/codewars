"""
Background
We all know about "balancing parentheses" (plus brackets, braces and chevrons) and even balancing characters that are identical.

Read that last sentence again, I balanced different characters and identical characters twice
and you didn't even notice... :)

Kata
Your challenge in this kata is to write a piece of code to validate that a supplied string is balanced.

You must determine if all that is open is then closed, and nothing is closed which is not already open!

You will be given a string to validate, and a second string, where each pair of characters defines an opening
and closing sequence that needs balancing.

You may assume that the second string always has an even number of characters.

Example
# In this case '(' opens a section, and ')' closes a section
is_balanced("(Sensei says yes!)", "()")       # => True
is_balanced("(Sensei says no!", "()")         # => False

# In this case '(' and '[' open a section, while ')' and ']' close a section
is_balanced("(Sensei [says] yes!)", "()[]")   # => True
is_balanced("(Sensei [says) no!]", "()[]")    # => False

# In this case a single quote (') both opens and closes a section
is_balanced("Sensei says 'yes'!", "''")       # => True
is_balanced("Sensei say's no!", "''")         # => False
"""


def is_balanced(source, caps):
    """
    Remove all characters from the string, except those in 'caps':
    """
    s_strip = "".join(map(lambda i: i if i in caps else '', source))
    """ 
    Create two lists: 
        -- containing a list of indexes of the "opening" elements of the modified source string
        -- containing a list of indexes of "closing" elements of the modified source string: 
    """
    left_part = [[i for i in range(len(s_strip)) if s_strip[i] == n] for n in caps[::2]]
    right_part = [[i for i in range(len(s_strip)) if s_strip[i] == n] for n in caps[1::2]]
    """ 
    The meaning of the comparison is that the sum of indices of the opened "correctly" closed element must be odd
    """
    if all(map(lambda x: x not in source, caps)):
        return True
    elif all(map(lambda x: x in source, caps)):
        return all(map((lambda x, y: (sum(x) + sum(y))//len(x) % 2 if len(x) == len(y) else 0), left_part, right_part))
    else:
        return False

print(is_balanced("(Sensei says yes!", "()"))
# print(is_balanced("(([(])Hello()))", "()[]")) Sensei says -yes-!
