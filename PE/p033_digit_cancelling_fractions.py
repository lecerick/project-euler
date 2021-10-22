"""
Problem 33
------------------------
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import math

def reduceFraction(a,b):
    gcd = math.gcd(a,b)
    # print(gcd)
    return (a//gcd,b//gcd)

digit_cancelling_fractions = []
nums = [int(str(n1)+str(n2)) for n1 in range(0,10) for n2 in range(0,10)]
nums.remove(0)
fractions = [(a,b) for a in nums for b in nums if a<b]
# print(fractions)

for f in fractions:
    numer = f[0]
    denom = f[1]
    if len(str(numer))!=1 and len(str(denom))!=1:
        n1 = int(str(numer)[0])
        n2 = int(str(numer)[1])
        d1 = int(str(denom)[0])
        d2 = int(str(denom)[1])
        if (n1==d1 and d1!=0 and d2!=0 and n2/d2==numer/denom) or (n1==d2 and d1!=0 and d2!=0 and n2/d1==numer/denom) or (n2==d1 and d1!=0 and d2!=0 and n1/d2==numer/denom) or (n2==d2 and d2!=0 and d1!=0 and n1/d1==numer/denom) : #
            digit_cancelling_fractions.append((numer,denom))

print(digit_cancelling_fractions)
numer = 1
denom = 1
for f in digit_cancelling_fractions:
    numer*=f[0]
    denom*=f[1]
answer = reduceFraction(numer,denom)
print('Answer = {}'.format(answer[1]))
