"""Method 1: Using dict() method.
Syntax: dict(list_comprehension)

>> ts = [(1, 2), (3, 4), (5, 6)]
>> dict(ts)
{1: 2, 3: 4, 5: 6}
>> gen = ((i, i+1) for i in range(1, 6, 2))
>> gen
<generator object <genexpr> at 0xb7201c5c>
>> dict(gen)
{1: 2, 3: 4, 5: 6}

"""

# Example 1:

data_name = ['bobby', 'ojaswi', 'rohith', 'gnanesh', 'bobby']
data_age = [23, 15, 8, 24, 20]

d1 = dict([(data_name[i], data_age[i]) for i in range(len(data_name))])
print(d1)

# Example 2:

data = [('bobby', 15), ('ojaswi', 11), ('rohith', 18), ('gnanesh', 14), ('bobby', 19)]
d2 = dict([(a, b) for a, b in data])
print(d2)


"""
Method 2: Using zip() with dict() method.
Syntax: dict(zip(key_list,value_list))
"""
# Example 1:

# create a list with student name
name = ['sravan', 'ojaswi', 'rohith', 'gnanesh', 'bobby']

# create a list with student age
age = [23, 21, 32, 11, 23]

# using dict method with zip()
d3 = dict(zip(name, age))

print(d3)


"""
Method 3: Using Iterable.
Syntax: {key: value for (key, value) in data}
"""
# Example:

# create a list comprehension with student age
data = [('sravan', 23), ('ojaswi', 15), ('rohith', 8), ('gnanesh', 4), ('bobby', 20)]

# display using iterable method
d4 = {key: value for (key, value) in data}

print(d4)


"""
Method 4: Add Filter
Syntax: {key: value for (key, value) in data condition}
"""
# Example:

# create a list comprehension with student age
data = [('sravan', 23), ('ojaswi', 15), ('rohith', 8), ('gnanesh', 4), ('bobby', 20)]

# create a dictionary with list
# comprehension if value is equal to 20
print({key: value for (key, value) in data if value == 20})

# create a dictionary with list
# comprehension if value is greater than to 10
print({key: value for (key, value) in data if value > 10})

# create a dictionary with list
# comprehension if key is sravan
print({key: value for (key, value) in data if key == 'sravan'})

