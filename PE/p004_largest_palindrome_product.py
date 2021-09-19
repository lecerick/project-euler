"""
Problem # 4
-------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math

def isPalindrome(N):
    """Takes a natural number N, returns a boolean stating whether N is a Palindrome number"""
    N_maxdigits = math.ceil(math.log10(N))
    i = 0
    while i<= int(N_maxdigits/2):
        digit_index_1 = i
        digit_index_2 = N_maxdigits - i - 1
        n1 = str(N)[digit_index_1: (digit_index_1+1)]
        n2 = str(N)[digit_index_2: (digit_index_2+1)]
        if n1!=n2:
            return False
        i+=1
    return True

def largestPalindrome(digits):
    """Returns the largest palindrome that can be made from the product of two natural numbers with input # of digits"""
    max_factor = int('9' * digits)
    min_factor = int('1'+ ('0' * (digits-1)))
    k = max_factor ** 2
    while k>0:
        if isPalindrome(k):
            for factor_candidate in range(min_factor, max_factor+1):
                if k % factor_candidate == 0:
                    if math.ceil(math.log10((k // factor_candidate)))==digits:
                        print('number: ' + str(k) + ' ..... factors: ' + str(factor_candidate) + ' ' + str((k // factor_candidate)))
                        return k
        k-=1

largestPalindrome(2)
largestPalindrome(3)
largestPalindrome(4)
