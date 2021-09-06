"""
Problem 3
---------
The prime factors of 13195 are 5, 7, 13 and 29. 
What is the largest prime factor of the number 600851475143 ?
"""

def smallestPrimeFactor(number):
    primes = [2]
    # We go through all i from 2 to number/2-1 and see if they are a prime divisor of the input number
    i = 2
    while i < number/2:
        # Assume at first that i is prime, then look for a counterexample (a divisor).
        i_has_divisor = False
        # We'll keep track of all the primes so it's easy to check if each new number i has a divisor.
        for j in range(0,len(primes)):
            if i % primes[j] == 0:
                # Found a divisor, time to exit the loop
                i_has_divisor = True
                break
        if i_has_divisor==False:
            # i is a new prime!
            # Is the input number divisible by i? If so, we found a prime factor.
            # Since we're incrementing upwards, this will occur when i is the smallest prime factor.
            if number % i == 0:
                return i
            # i is prime but not a divisor of number, so we simply add it to the list of primes and keep looking for candidates
            else:
                primes.append(i)
        i+=1
    # If we've gone through all possible numbers and not found a prime factor, then the input number must itself be a prime
    return number

def largestPrimeFactor(number):
    # Find a prime factor, then factorize the result of number / prime factor. Repeat until you have a list of all prime factors of the input number.
    prime_factors = []
    x = number
    while x>1:
        y = smallestPrimeFactor(x)
        prime_factors.append(y)
        x = int(x / y)
    # The solution is the maximum of all the prime factors.
    return max(prime_factors)

print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))