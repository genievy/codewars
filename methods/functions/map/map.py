"""
map() function returns a map object(which is an iterator) of the results after applying the given
function to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)

or:

map(function, iterable[, iterable1, iterable2,..., iterableN])

Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

Returns :

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

NOTE : The returned value from map() (map object) then can be passed
to functions like list() (to create a list), set() (to create a set) .

"""

# CODE 1:

# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# CODE 2

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# CODE 3

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# CODE 4

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


"""
RU:
map() применяет функцию к каждому элементу в итерируемом цикле и возвращает новый итератор, 
который по запросу возвращает преобразованные элементы. function может быть любая функция Python, 
которая принимает принимать аргументы, равное количеству итераций, которые вы передаете map().

Примечание. Первый аргумент map() — это объект функция, что означает, что вам нужно передать функцию, не вызывая ее. 
То есть без пары скобок.

Первый аргумент map() — функция преобразования. Другими словами, это функция, 
которая преобразует каждый исходный элемент в новый (преобразованный) элемент. 
Несмотря на то, что документация Python вызывает эту функцию аргумента, она может быть любой вызываемой Python. 
Сюда входят встроенные функции, классы, методы, лямбда-функции и пользовательские функции.

Операция, выполняемая map(), обычно известна как сопоставление, 
потому что она сопоставляет каждый элемент во входном итерируемом элементе с новым элементом в итоговом итерируемом. 
Для этого map() применяет функцию преобразования ко всем элементам во входной итерации.
"""


