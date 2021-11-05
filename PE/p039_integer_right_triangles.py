"""
Problem #39
------------------
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

def is_square(n):
    return n == math.isqrt(n) ** 2

solutions = [set({}) for p in range(0,1000)]
for a in range(1,999):
    for b in range(1,999):
        if is_square(a**2 + b**2):
            c = int(math.sqrt(a**2 + b**2))
            p = a + b + c
            if p < 1000:
                solutions[p].add((a,b,c))

max = 0
for p in range(0,1000):
    if len(solutions[p])>max:
        max = len(solutions[p])
        answer = p
    # if len(solutions[p])>0:
    #     print('{}: {}'.format(p,solutions[p]))

print('Max @ {} with {} solutions'.format(answer,len(solutions[answer])))
print(solutions[answer])