"""
Problem #26
--------------
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def cycleLength(n: int) -> int:
    """Returns the length of the recurring cycle of 1/n
    e.g. cycleLength(7) -> 6, because 1/7 = 0.(142857)"""
    digits = []
    remainders = {}
    i = 10
    counter = 1
    while True:
        digits.append(i//n)
        remainder = i % n
        # print(remainders)
        if remainder in remainders:
            return counter - remainders[remainder]
            break
        remainders[remainder] = counter
        counter+=1
        i= remainder * 10
    print('N='+str(n)+' 0.'+''.join(str(e) for e in digits))

max = 0
max_i = 0
for i in range(2,1000):
    print('{} cyclelength = {}'.format(i,cycleLength(i)))
    if cycleLength(i)>max:
        max = cycleLength(i)
        max_i = i
print('1/{} has the max cycle of {}'.format(max_i, max))
print(1/max_i)