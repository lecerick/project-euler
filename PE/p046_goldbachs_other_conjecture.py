"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

def is_square(n: int) -> bool:
    return math.isqrt(n) ** 2 == n

threshold = 10 ** 4
is_prime = [True for n in range(0,threshold)]
primes = []
is_prime[0]=False
is_prime[1]=False
for n in range(2,threshold):
    if is_prime[n]==True:
        for multiple in range(2 * n, threshold, n):
            is_prime[multiple]=False
        primes.append(n)
    elif n % 2 == 1:
        can_be_written = False
        for p in primes:
            maybe_square = (n - p) // 2
            if (n-p) % 2 == 0 and is_square(maybe_square):
                can_be_written = True
        if not can_be_written:
            print('{} is an odd composite & cannot be written as the sum of a prime and twice a square'.format(n))
