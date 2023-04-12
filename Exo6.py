"""
Write an algorithm who can calculate the factorial of numbers.
"""

# Réponse :
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5))
