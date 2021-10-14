"""
Problem #10
-----------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from timeit import default_timer as timer
from datetime import timedelta

def sumOfPrimes1(threshold):
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

def sumOfPrimes2(threshold):
    primeset = set({})
    sum = 0
    for i in range(2,threshold):
        if not any(i%p==0 for p in primeset):
            primeset.add(i)
            sum+=i
    return sum

def sumOfPrimes3(threshold):
    """Returns the sum of all primes below the given threshold"""
    sum = 2
    primes = set({})
    for i in range(2,threshold):
        has_divisor = False
        for j in primes:
            if i % j == 0:
                has_divisor = True
                break
        if has_divisor == False:
            sum+=i
            primes.add(i)
        i+=1
    return sum

def sumOfPrimes4(threshold):
    sum = 0
    numcheck = [True for n in range(2,threshold)]
    return sum

# def sumOfPrimes5(threshold): 
#     sum = 0
#     to_check = [i for i in range(2,threshold)]
#     while len(to_check)>0:
#         i = to_check[0]
#         for m in range(1,threshold//i+1):
#             if i*m in to_check:
#                 to_check.remove(i*m)
#         sum+=i
#     return sum


# print(str(sumOfPrimes1(10)))
# print(str(sumOfPrimes1(2000000)))

for i in range(1,6):
    # print("10 ** {}".format(i))
    # start = timer()
    # answer = sumOfPrimes1(10 ** i)
    # end = timer()
    # print("METHOD1: {}  {} ".format(answer,str(timedelta(seconds=end-start))))
    # start = timer()
    # answer = sumOfPrimes2(10 ** i)
    # end = timer()
    # print("METHOD2: {}  {} ".format(answer,str(timedelta(seconds=end-start))))
    start = timer()
    answer = sumOfPrimes3(10 ** i)
    end = timer()
    print("METHOD3: {}  {} ".format(answer,str(timedelta(seconds=end-start))))
    start = timer()
    answer = sumOfPrimes4(10 ** i)
    end = timer()
    print("METHOD4: {}  {} ".format(answer,str(timedelta(seconds=end-start))))
    print("---------------------------------------------------------------------------")