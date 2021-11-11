"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
import itertools
def replacement_list(n: int) -> list:
    # takes a number n and returns a list of all possible replacements
    # e.g. if n is 13, returns ['*3', '1*']
    repl_list = []
    permutes = [''.join(perm) for perm in itertools.product(['0','1'],repeat=len(str(n)))]
    permutes.remove('1'*len(str(n)))
    permutes.remove('0'*len(str(n)))
    for permute in permutes:
        n_repl_str = ''.join([str(n)[i] if permute[i]=='0' else '*' for i in range(len(str(n)))])
        repl_list.append(n_repl_str)
    return repl_list

# Generate a list of primes using the seive method
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

for p in primes:
    replace_keys = replacement_list(p) #['*3','56**3']
    for x in replace_keys:
        family = []
        for digit in range(0,10):
            n_str = ''
            for char in x:
                if char=='*':
                    n_str+=str(digit)
                else:
                    n_str+=char
            n = int(n_str)
            if n in primes and len(str(n))==len(x):
                family.append(n)
        if len(family)==8:
            print('{} is the smallest of the family {}'.format(min(family),family))
            break
