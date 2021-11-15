"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
import itertools

def solution():
    x = 1
    while True:
        x_is_solution = True
        perms = [int(''.join(perm)) for perm in itertools.permutations(str(x),len(str(x)))]
        for multiplier in range(2,7):
            if x * multiplier not in perms:
                x_is_solution=False
        if x_is_solution:
            return x
        x+=1
    return -1

print(solution())