"""
Problem #27
------------
This problem has a lot of formulas that don't copy/paste, so check out the description here: https://projecteuler.net/problem=27
"""

# Generate an ordered list of all primes under the limit
limit = 200000


class PrimeList():
    def __init__(self, limit) -> None:
        self.primeset = set({})
        self.limit = 2
        self.addPrimes(limit)

    def addPrimes(self, new_limit):
        for i in range(self.limit,new_limit):
            if not any(i%p==0 for p in self.primeset):
                self.primeset.add(i)
        self.limit = new_limit
    
    def printSorted(self):
        print(sorted(self.primeset))

P = PrimeList(1000)

max = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        f_n = 2
        n = 0
        while f_n in P.primeset:
            f_n = n ** 2 + a * n + b
            # print(f_n)
            if f_n > limit:
                P.addPrimes(f_n+1)
            n+=1
        if n>max:
            max = n
            max_a = a
            max_b = b
            print('Max number of consecutive primes: {}, a = {}, b ={}'.format(max,max_a,max_b))
        
P.printSorted()
print(max_a*max_b)

# Tests...
# a = 1
# b = 41
# n = 0
# while True:
#     f_n = n ** 2 + a * n + b
#     if f_n not in primeset:
#         break
#     n+=1
# print(n)