"""
Problem #7
---------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def nthPrime(n):
    primes = [2]
    num_primes = 1
    i = 3
    while num_primes <n:
        has_divisor = False
        for j in range(0,len(primes)):
            if i % primes[j] == 0:
                has_divisor = True
                break
        if has_divisor == False:
            primes.append(i)
            num_primes +=1
        i+=1
    return primes[len(primes)-1]

print(nthPrime(6))
print(nthPrime(10001))