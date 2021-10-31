"""
Problem #36
-----------------
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
import math

def isPalindrome(n: int) -> bool:
    digits = len(str(n))
    for i in range(0,digits//2):
        if str(n)[i] != str(n)[digits-1-i]:
            return False
    return True

def binaryForm(n: int) -> int:
    bform = ''
    digits = math.floor(math.log(n,2))
    while digits >=0:
        new_digit = n // (2**digits)
        bform+=str(new_digit)
        n = n - (2**digits) * new_digit
        digits-=1
    return int(bform)

def sumOfDoublePalindromes(threshold):
    sum = 0
    for n in range(1,threshold):
        b_n = binaryForm(n)
        if isPalindrome(n) and isPalindrome(b_n): 
            print('{} ({} in binary) is a double-palindrome'.format(n,b_n))
            sum+=n
    return sum

print('Answer: {}'.format(sumOfDoublePalindromes(10**6)))