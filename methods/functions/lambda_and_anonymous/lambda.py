"""
Python Lambda Functions are anonymous function means that the function is without a name. As we already know
that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define
an anonymous function in Python.

Syntax: lambda arguments: expression

This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
It has various uses in particular fields of programming, besides other types of expressions in functions.
"""

# Example 1: Python Lambda Function with List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

# Example 2: Python Lambda Function with if-else (using Max lambda function to find the maximum of two integers)

# Example of lambda function using if-else

maximum = lambda a, b: a if (a > b) else b

print(maximum(1, 2))

# Example 3: Python Lambda with Multiple statements
"""
Lambda functions does not allow multiple statements, however, we can create two lambda functions and then call the other
lambda function as a parameter to the first function. Let’s try to find the second maximum element using lambda.
"""

List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)


"""
Using lambda() Function with filter()
"""

# Example 1: Filter out all odd numbers using filter() and lambda function
"""Here, lambda x: (x % 2 != 0) returns True or False if x is not even. 
Since filter() only keeps elements where it produces True, thus it removes all odd numbers that generated False."""

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# Example 2: Filter all people having age more than 18, using lambda and filter() function

# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))

print(adults)


"""
Using lambda() Function with map()
The map() function in Python takes in a function and a list as an argument. The function is called 
with a lambda function and a list and a new list is returned which contains all the lambda modified items 
returned by that function for each item. 
"""

# Example 1: Multiply all elements of a list by 2 using lambda and map() function

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)

# Example 2: Transform all elements of a list to upper case using lambda and map() function

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)


"""
Using lambda() Function with reduce()
The reduce() function in Python takes in a function and a list as an argument. The function is called 
with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation 
over the pairs of the iterable. The reduce() function belongs to the  functools module. 
"""

# Example 1: Sum of all elements in a list using lambda and reduce() function

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

# Example 2: Find the maximum element in a list using lambda and reduce() function

# python code to demonstrate working of reduce()
# with a lambda function

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
