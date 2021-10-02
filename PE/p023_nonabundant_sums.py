"""
Problem #23
---------------
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis,
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
limit = 28124

# Generate an ordered list of all primes under the limit
primes = []
i = 2
while i < limit:
    i_has_divisor = False
    for j in range(0,len(primes)):
        if i % primes[j] == 0:
            i_has_divisor = True
            break
    if i_has_divisor==False:
            primes.append(i)
    i+=1
# print(primes)

def smallestPrimeFactor(n):
    for i in range(0,len(primes)):
        if n % primes[i] == 0:
            return primes[i]

def primeFactorization(n):
    # returns a list of all prime factors of N
    primefactors = []
    i = n
    while i>1:
        prime = smallestPrimeFactor(i)
        if primefactors.count(prime)==0:
            primefactors.append(prime)
        i = i // prime
    return primefactors

def properDivisors(n):
    prime_factors = primeFactorization(n)
    if n in prime_factors:
        prime_factors.remove(n)
    answer = prime_factors
    for i in range(0,len(prime_factors)):
        max_power = math.floor(math.log(n, prime_factors[i]))
        for power in range(2,max_power):
            if n % (prime_factors[i]**power) == 0:
                answer.append(prime_factors[i]**power)
        for j in range(0,len(answer)):
            x = prime_factors[i]*answer[j]
            if n % x == 0 and x not in answer and x<n:
                answer.append(x)
    answer.append(1)
    return answer

print(sorted(primeFactorization(100000)))
print(sorted(properDivisors(100000)))

# Create a list of abundant numbers
# abundant_nums = []
# for i in range(1,limit):
#     # print('Proper divisors of {}: {}'.format(i,properDivisors(i)))
#     if i<sum(properDivisors(i)):
#         abundant_nums.append(i)
# print(abundant_nums)

# Create the set of abundant sums
# abundant_sums = set()
# for i in range(0,len(abundant_nums)):
#     for j in range(i+1,len(abundant_nums)):
#         abundant_sums.add(abundant_nums[i]+abundant_nums[j])

# Calculate the sum of all nonabundant sums
# answer=0
# for i in range(1,limit):
#     if i not in abundant_sums:
#         answer+=i
# print(answer)