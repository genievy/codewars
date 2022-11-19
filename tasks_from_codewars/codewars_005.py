"""
Who likes it?

DESCRIPTION:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""


# my code
def likes(names):
    t = ['no one', 'and', 'others']
    if len(names):
        if len(names) < 4:
            try:
                n = f'{names[0]}, {names[1]} {t[1]} {names[2]} like this'
            except:
                try:
                    n = f'{names[0]} {t[1]} {names[1]} like this'
                except:
                    n = f'{names[0]} likes this'
        else:
            n = f'{names[0]}, {names[1]} {t[1]} {str(len(names)-2)} {t[2]} like this'
    else:
        n = f'{t[0]} likes this'
    return n


lista_names = []
# lista_names = ["Peter"]
# lista_names = ["Jacob", "Alex"]
# lista_names = ["Max", "John", "Mark"]
# lista_names = ["Alex", "Jacob", "Mark", "Max"]
print(likes(lista_names))



# fine code

# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return "%s likes this" % names[0]
#     elif len(names) == 2:
#         return "%s and %s like this" % (names[0], names[1])
#     elif len(names) == 3:
#         return "%s, %s and %s like this" % (names[0], names[1], names[2])
#     else:
#         return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
