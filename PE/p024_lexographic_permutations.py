"""
Problem #24
----------------
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

digits = 10

num_permutations = math.factorial(digits)
max_permutation = [x for x in range(0,digits)]
print('------------------------------')
print('Number of digits permuted: {}'.format(digits))
print('Number of permutations: {}'.format(num_permutations))
print('Lexographic max: {}'.format(''.join(str(e) for e in max_permutation)))
print('------------------------------')
nth = 1000000
print('Finding lexographic permutation #{}'.format(nth))

n = num_permutations
i = digits
current_num = nth
answer = []
choices = max_permutation
while i>1:
    tranche_size = n//i
    position = (current_num - 1) // tranche_size
    # print('i={}: Tranche Size = {}  Current Num = {}, N = {},  Position = {}, Choices = {}'.format(i, tranche_size, str(current_num).ljust(10,' '), str(n).ljust(10,' '), position, choices))
    n_i = choices[position]
    answer.append(n_i)
    choices.remove(n_i)
    n = tranche_size
    current_num = current_num - (position)*(tranche_size)
    i-=1
answer.append(choices[0])
print('Answer: {}'.format(''.join(str(e) for e in answer)))

