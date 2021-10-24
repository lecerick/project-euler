"""
Problem 34
-----------------
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math
digit_factorials = set({})
for n in range(3,10000):
    if n == sum([math.factorial(int(char)) for char in str(n)]):
        digit_factorials.add(n)
        print(n)