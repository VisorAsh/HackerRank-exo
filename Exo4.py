"""
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following: 123...n. Example: n = 5, print the string 12345.
"""

# Réponse :
n = int(input())

for i in range(1, n + 1):
    print(i, end="") # on utilise le paramètre end pour éviter le saut de ligne après chaque nombre.
