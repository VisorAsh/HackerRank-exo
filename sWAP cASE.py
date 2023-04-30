"""
Task
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

# Réponse :
# 1er cas :
def swap_case(s):
    new_word = ""
    for i in s:
        if i == i.upper():
            new_word += i.lower()
        elif i == i.lower():
            new_word += i.upper()
        else:
            new_word += i
    return new_word

# 2ème cas :
def swap_case(s):
    return s.swapcase()    # Fonction permettant de swaper les majiscules et les minuscules.

# Suite de la logique :
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
