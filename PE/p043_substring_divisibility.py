"""
Problem #43
-------------
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools
answer_set = set({})
pandigital_numbers = set({int(''.join(i)) for i in itertools.permutations('0123456789',10)})
# pandigital_numbers = set({1406357289})
# print(pandigital_numbers)
for n in pandigital_numbers:
    primes = [2,3,5,7,11,13,17]
    conditions = [int(str(n)[i:i+3]) % primes[i-1] == 0 for i in range(1,8)]
    if all(conditions):
        answer_set.add(n)
print(answer_set)
print(sum(answer_set))
