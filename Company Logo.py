"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G,O,E.
"""

# En tête :
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()


# Reponse :
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()

    counter = {}
    for count in s:
        if count in counter:
            counter[count] += 1
        else:
            counter[count] = 1

    topThree = sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:3]

    for count, frequence in topThree:
        print(count, frequence)
