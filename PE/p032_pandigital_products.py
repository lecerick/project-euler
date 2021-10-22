"""
Problem 32
---------------------
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import itertools

pandigital_products = []
for t in list(itertools.permutations('123456789',9)):
    s=''.join(t)
    for m1_len in range(1,9):
        for m2_len in range(1,9-m1_len):
            m1 = int(s[0:m1_len])
            m2 = int(s[m1_len:(m2_len+m1_len)])
            # print(m2_len+m1_len)
            p = int(s[(m2_len+m1_len):10])
            if m1 * m2 == p and p not in pandigital_products:
                print('{} --> {} * {} = {}'.format(s,m1,m2,p))
                pandigital_products.append(p)

print(pandigital_products)
print('Sum of {} pandigital products is {}'.format(len(pandigital_products), sum(pandigital_products)))