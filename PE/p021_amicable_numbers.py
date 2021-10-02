"""
Problem #21
----------------
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; thus d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
import math
from p012_highly_divisible_triangular_number import primeFactorization

def properDivisors(n):
    primes = primeFactorization(n)
    if n in primes:
        primes.remove(n)
    answer = primes
    for i in range(0,len(primes)):
        # print('prime: {}'.format(primes[i]))
        max_power = math.floor(math.log(n, primes[i]))
        for power in range(2,max_power):
            if n % (primes[i]**power) == 0:
                answer.append(primes[i]**power)
        for j in range(0,len(answer)):
            x = primes[i]*answer[j]
            if n % x == 0 and x not in answer and x<n:
                answer.append(x)
    answer.append(1)
    # answer.sort()
    return answer

# amicable_nums = []
# for i in range(1,10000):
#     if i in amicable_nums:
#         pass
#     s = sum(properDivisors(i))
#     if i==sum(properDivisors(s)) and i!=s:
#         if i not in amicable_nums:
#             amicable_nums.append(i)
#         if s not in amicable_nums:
#             amicable_nums.append(s)
#         print('Found a pair of amicable numbers! {} and {}'.format(i, s))

# print(amicable_nums)
# print(sum(amicable_nums))