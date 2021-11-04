"""
Problem #41
-------------
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
from timeit import default_timer as timer
from datetime import timedelta

#utilize the sieve method to pre-load the list of primes
start = timer()

pandigital_prime = set({})
threshold = 10**7
sieve = [1 for i in range(0,threshold)]
sieve[0] = 0
sieve[1] = 0
for n in range(2,threshold):
    if sieve[n]==1:
        for multiple in range(n*2,threshold,n):
            sieve[multiple]=0
        if all([str(i) in str(n) for i in range(1,len(str(n))+1)]):
            pandigital_prime.add(n)
print(sorted(pandigital_prime))
end = timer()

print('There are {} pandigital primes, the largest of which is {} (time = {})'.format(len(pandigital_prime),max(pandigital_prime),str(timedelta(seconds=end-start))))
# took 8 minutes 52 seconds using threshold = 10 ** 9
# get the same answer is 5 seconds if using 10 ** 7, but to exhaustively prove the answer you have to use 10 ** 9