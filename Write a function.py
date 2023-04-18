"""
Task
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. A faire : Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function. 
"""

# Réponse :
def is_leap(year):
    leap = False
    # Write your logic here
    # Si l'année est divisible par 4
    if year % 4 == 0:
        # Si elle est divisible par 100, elle doit aussi être divisible par 400 pour être bissextile
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        # Si elle n'est pas divisible par 100, elle est bissextile
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))
