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
    i = 10
    while True:
        digits.append(i//n)
        i = i % n
        i*=10
        if len(digits)>100:
            break
    print('N='+str(n)+' 0.'+''.join(str(e) for e in digits))
    # stop when you have a remainder you already saw??
    return 0


for i in range(1,30):
    cycleLength(i)