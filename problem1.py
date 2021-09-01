"""
Problem 1
---------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def bruteforce(threshold):
    multiples = []
    i = 1
    while i*3 < threshold:
        multiples.append(i*3)
        i+=1
    i = 1
    while i*5 < threshold:
        if(i*5 % 3 != 0):
            multiples.append(i*5)
        i+=1
    sum = 0
    for index in range(0,len(multiples)):
        sum = sum + multiples[index]
    return(sum)

def clever(threshold):
    """Identity: SUM of k from k=1 to k=n == 0.5n(n+1)
    The efficiency in this method is derived from the fact that you only need the sum, not the whole array of items in the series
    The desired series consists of the union of the "multiples of threes" series and the "multiples of fives" series
    But since both series include the "multiples of 15" series, we must remove it so as to not duplicate.
    """
    n3 = (threshold -1)// 3
    n5 = (threshold -1)// 5
    n15 = (threshold -1) // 15
    sum5s  = 5 * 0.5 * n5  * (n5 + 1)
    sum3s  = 3 * 0.5 * n3 * (n3 + 1)
    sum15s = 15 * 0.5 * n15 * (n15 + 1)
    sum = sum5s + sum3s - sum15s
    return int(sum)

print("brute force")
print(bruteforce(10))
print(bruteforce(1000))
print(bruteforce(1000000))
print("\n")
print("clever")
print(clever(10))
print(clever(1000))
print(clever(1000000))
