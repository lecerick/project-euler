"""
Problem #35
----------------
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
import itertools

#utilize the sieve method to pre-load the list of primes
threshold = 10 ** 6
prime = set({})
not_prime = set({})
for n in range(2,threshold):
    if n in not_prime:
        pass
    else:
        prime.add(n)
        for multiple in range(n*2,threshold,n):
            not_prime.add(multiple)
prime = sorted(prime)
# print(prime)

def rotate(n: int, clicks: int) -> int:
    clicks = clicks % len(str(n))
    st1 = str(n)[0:len(str(n))-clicks]
    st2 = str(n)[len(str(n))-clicks:len(str(n))]
    return int(st2+st1)

def rotations(n: int) -> list:
    rotations = [n]
    return [rotate(n,click) for click in range(0,len(str(n)))]

#for each prime, check its rotations against the set of primes
circular_primes = set({})
for p in prime:
    digits = [char for char in str(p)]
    if p < 10 or not('0' in digits or '2' in digits or '4' in digits or '5' in digits or '6' in digits or '8' in digits):
        is_circular_prime = True
        for rotation in rotations(p):
            if rotation not in prime:
                is_circular_prime = False
                # print('{} not circular because {} not prime'.format(p,rotation))
                break
        if is_circular_prime:
            circular_primes.add(p)
            
print(sorted(circular_primes))
print(len(circular_primes))