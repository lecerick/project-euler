"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
import itertools
from timeit import default_timer as timer
from datetime import timedelta

def replacement_set(n: int) -> list:
    repl_list = set({})
    permutes = [''.join(perm) for perm in itertools.product(['0','1'],repeat=len(str(n)))]
    permutes.remove('1'*len(str(n)))
    permutes.remove('0'*len(str(n)))
    for permute in permutes:
        is_viable_permute=True
        astrisks = [str(n)[i] for i in range(len(str(n))) if permute[i]=='1']
        for item in astrisks:
            if item!=astrisks[0]:
                is_viable_permute=False
        if is_viable_permute:
            n_repl_str = ''.join([str(n)[i] if permute[i]=='0' else '*' for i in range(len(str(n)))])
            repl_list.add(n_repl_str)
    return repl_list
    # repl_set = set({})
    # for i in range(0,10):
    #     if str(i) in str(n):
    #         n_str = ''
    #         for char in str(n):
    #             if char==str(i):
    #                 n_str+='*'
    #             else:
    #                 n_str+=char
    #         repl_set.add(n_str)
    # return repl_set
        
# print(replacement_set(56001))

def solution():
    # Generate a list of primes using the seive method
    families = dict()
    threshold = 10 ** 6
    is_prime = [True for n in range(0,threshold)]
    is_prime[0]=False
    is_prime[1]=False
    primes = []
    for i in range(2,threshold):
        if is_prime[i]==True:
            for multiple in range(i*2,threshold,i):
                is_prime[multiple]=False
            primes.append(i)
            replace_keys = replacement_set(i) #['*3','56**3']
            for key in replace_keys:
                if key not in families:
                    families[key]= []
                families[key].append(i)
    for family in families:
        if len(families[family])==8:
            print(family)
            print('{} is the smallest of the family {}'.format(min(families[family]),families[family]))
            return(min(families[family]))
    print(families['56**3'])
    # print(families)

start = timer()
solution()
end = timer()
print(str(timedelta(seconds=end-start)))