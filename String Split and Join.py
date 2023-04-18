"""
In Python, a string can be split on a delimiter.

Exemple
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

# En tête
def split_and_join(line):
    # write your code here
    print('Hello World !') # Moi même j'ai rajouté

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Réponse : (ici on modifie l'entête en rajoutant list()au map du début)
def split_and_join(line):
    # write your code here
    a = line.split(" ")
    b = "-".join(a)
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
