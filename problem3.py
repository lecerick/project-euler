"""
Problem 3
---------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
# def isPrime(number):
def smallestPrimeFactor(number):
    primes = [2]
    i = 3
    while i <= number/2:
        # Assume at first that i is prime
        i_has_divisor = False
        # Iterate through list of all primes smaller than i
        for j in range(0,len(primes)):
            if i % primes[j] == 0:
                # found a divisor, thus i is not prime (& hence not a candidate), time to exit the loop
                i_has_divisor = True
                break
        # We have gone through the list of primes and determined whether i is a new prime number
        if i_has_divisor==False:
            primes.append(i)
            # As soon as the input number is divisible by a prime, we return & exit the method.
            # Since we're incrementing upwards, this will occur for the smallest prime factor.
            if number % i == 0:
                return i
        i+=1
    # If we've gone through all the numbers and not found a prime factor, then the input number must itself be a prime
    return number

def largestPrimeFactor(number):
    prime_factors = []
    x = number
    while x>1:
        y = smallestPrimeFactor(x)
        prime_factors.append(y)
        x = int(x / y)
    return max(prime_factors)


print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))