"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

threshold = 10 ** 6
prime_factors = [0 for n in range(0,threshold)]
primes = []
for n in range(2,threshold):
    if prime_factors[n]==0:
        for multiple in range(2 * n, threshold, n):
            prime_factors[multiple]+=1
        primes.append(n)
for i in range(0,threshold-4):
    if prime_factors[i]==4 and prime_factors[i+1]==4 and prime_factors[i+2]==4 and prime_factors[i+3]==4:
        print(i)