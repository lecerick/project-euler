"""
Problem #10
-----------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def sumOfPrimes(threshold):
    """Returns the sum of all primes below the given threshold"""
    sum = 2
    i=3
    primes = [2]
    while i<threshold:
        has_divisor = False
        for j in range(0,len(primes)):
            if i % primes[j] == 0:
                has_divisor = True
                break
        if has_divisor == False:
            sum+=i
            primes.append(i)
        i+=1
    return sum


print(str(sumOfPrimes(10)))
print(str(sumOfPrimes(2000000)))
