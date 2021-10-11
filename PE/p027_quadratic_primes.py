"""
Problem #27
------------
This problem has a lot of formulas that don't copy/paste, so check out the description here: https://projecteuler.net/problem=27
"""

import math
limit = 1000000

# Generate an ordered list of all primes under the limit
primes = []
primeset = set({})
i = 2
while i < limit:
    i_has_divisor = False
    for j in range(0,len(primes)):
        if i % primes[j] == 0:
            i_has_divisor = True
            break
    if i_has_divisor==False:
            primes.append(i)
            primeset.add(i)
    i+=1
# print(primes)

# Tests...
# a = 1
# b = 41
# n = 0
# while True:
#     f_n = n ** 2 + a * n + b
#     if f_n not in primes:
#         break
#     n+=1
# print(n)

max = 0
for a in range(-100,100):
    for b in range(-100,100):
        f_n = -1
        n = 0
        while f_n not in primeset:
            f_n = n ** 2 + a * n + b
            if f_n > limit:
                print("WARNING, PRIME LIMIT EXCEEDED AT {}, n={}, a={}, b={}".format(f_n,n,a,b))
                break
            n+=1
        if n>max:
            max = n
            max_a = a
            max_b = b

print('Max number of consecutive primes: {}, a = {}, b ={}'.format(max,max_a,max_b))
        


