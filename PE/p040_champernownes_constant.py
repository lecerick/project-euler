"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
c = '0.123456789'
nums = [0,1,2,3,4,5,6,7,8,9]
n = 1
while len(c)<=(10**6):
    c+= ''.join([str(n)+str(i) for i in nums])
    n+=1

answer = 1
for x in range(0,6):
    dx = c[10**x+1]
    print('d{} = {}'.format(10**x,dx))
    answer*=int(dx)
print(answer)