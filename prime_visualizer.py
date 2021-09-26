"""
Generates prime numbers and visualizes them
"""
import matplotlib.pyplot as plt

primes = [2]
num_primes = 1
i = 3
while num_primes <100:
    has_divisor = False
    for j in range(0,len(primes)):
        if i % primes[j] == 0:
            has_divisor = True
            break
    if has_divisor == False:
        primes.append(i)
        num_primes +=1
    i+=1

print(primes)