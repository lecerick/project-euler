'''
Problem #9
--------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def pythagoreanTriplets(N):
    """Prints the first N pythogorean triplets and their sum"""
    found_triplets = 0
    c = 1
    while found_triplets<N:
        for i in range(1,c):
            j = math.sqrt(c**2 - i**2)
            if j % 1 == 0 and i!=j:
                if j<i:
                    a = int(j)
                    b = int(i)
                else:
                    b = int(j)
                    a = int(i)
                sum = int(a+b+c)
                print('TRIPLET #'+str(found_triplets+1)+': '+str(a)+', '+str(b)+', '+str(c)+', sum= '+str(sum))
                print(str(a**2+b**2)+' = '+str(c**2))
                found_triplets+=1
                break
        c+=1

def pythagoreanTripletSum1000():
    c = 1
    while True:
        for i in range(1,c):
            j = math.sqrt(c**2 - i**2)
            if j % 1 == 0 and i!=j:
                if j<i:
                    a = int(j)
                    b = int(i)
                else:
                    b = int(j)
                    a = int(i)
                sum = int(a+b+c)
                if sum == 1000:
                    product = str(a * b * c)
                    print(str(a)+', '+str(b)+', '+str(c)+', sum= '+str(sum)+', product= '+str(product))
                    return product
        c+=1

# pythagoreanTriplets(100)
pythagoreanTripletSum1000() 