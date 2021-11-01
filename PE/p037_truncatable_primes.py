"""
Problem 37
-------------------
The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

#utilize the sieve method to pre-load the list of primes
threshold = 10 ** 6
prime = set({})
truncatable_prime = set({})
not_prime = set({})
for n in range(2,threshold):
    if n in not_prime:
        pass
    else:
        prime.add(n)
        if n > 10:
            is_truncatable_prime = True
            for i in range(1,len(str(n))):
                truncated_n1 = int(str(n)[i:len(str(n))]) 
                truncated_n2 = int(str(n)[0:len(str(n))-i])
                if truncated_n1 not in prime or truncated_n2 not in prime:
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_prime.add(n)
        for multiple in range(n*2,threshold,n):
            not_prime.add(multiple)
print(sorted(truncatable_prime))
print('There are {} truncatable primes, summing to {}'.format(len(truncatable_prime),sum(truncatable_prime)))