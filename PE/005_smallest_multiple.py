"""
Problem #5
------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math

def smallestMultiple(N):
    """returns the smallest number that is a multiple of all natural numbers n <= N"""
    # Generate a list of all primes <= N
    primes = [2]
    n = 3
    while n<=N:
        n_has_primefactor = False
        for i in range(0,len(primes)):
            if n % primes[i] == 0:
                n_has_primefactor = True
                break
        if n_has_primefactor!=True:
            # found a new prime
            primes.append(n)
        n+=1
    # Note that you have to account for orders of primes, e.g. the answer for N=10 must be divisble not just by 2, but by 2 ** 3 = 8
    # So, once you've found all the primes, determine the highest order of each prime that is <=N. The answer will be the product of all the primes to their highest order.
    smallest_multiple = 1
    for i in range(0,len(primes)):
        highest_order = math.floor(math.log(N,primes[i]))
        smallest_multiple = smallest_multiple * (primes[i] ** highest_order)
    return smallest_multiple

print(smallestMultiple(10))
print(smallestMultiple(20))
