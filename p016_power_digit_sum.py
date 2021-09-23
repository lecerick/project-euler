"""
Problem #16
-------------------
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""

n = 2 ** 1000
strn = str(n)
sum = 0
for i in range(1,len(strn)+1):
    digit = int(strn[i-1:i])
    sum+=digit
print(strn)
print(sum)