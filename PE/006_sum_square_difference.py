"""
Problem #6
------------
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from timeit import default_timer as timer
from datetime import timedelta

def bruteforce(N):
    x = 0
    y = 0
    for i in range(1,N+1):
        x += i ** 2
        y += i
    y = y ** 2
    answer = y - x
    return answer

def clever(N):
    """ Identities: 
    Sigma(n**2) == n * (n+1) * (2n+1) / 6 
    Signma(n) == n * (n+1) / 2 """
    sum_of_squares = N * (N+1) * (2*N+1) / 6
    square_of_sum = (N * (N+1) / 2) ** 2
    return int(square_of_sum - sum_of_squares)

def cleverer(N):
    """ Identities: 
    Sigma(n**2) == n * (n+1) * (2n+1) / 6 
    Signma(n) == n * (n+1) / 2 """
    sum_of_squares = N * (N+1) * (2*N+1) // 6
    square_of_sum = (N * (N+1) // 2) ** 2
    return int(square_of_sum - sum_of_squares)

# print(bruteforce(10))
# print(clever(10))
# print(bruteforce(100))
# print(clever(100))

for i in range(1,10+1):
    print("N = 10 ** "+str(i))
    start = timer()
    print("BRUTE FORCE METHOD:  "+str(bruteforce(10 ** i)))
    end = timer()
    print("BRUTE FORCE RUNTIME: "+str(timedelta(seconds=end-start)))
    start = timer()
    print("CLEVER METHOD:       "+ str(cleverer(10 ** i)))
    end = timer()
    print("CLEVER RUNTIME:      "+str(timedelta(seconds=end-start)))
    print("---------------------------------------------------------------------------")