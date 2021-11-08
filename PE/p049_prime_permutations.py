"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import itertools

# Generate list of primes using the sieve method
threshold = 10 ** 4
prime_factors = [True for n in range(0,threshold)]
primes = []
for n in range(2,threshold):
    if prime_factors[n]==True:
        for multiple in range(2 * n, threshold, n):
            prime_factors[multiple]=False
        primes.append(n)

# Test each of the relevant primes for the condition
for p in [p for p in primes if p>1000 and p<10000]:
    p_permutations = [int(''.join(tup)) for tup in itertools.permutations(str(p),4)]
    p_newterms = [n for n in p_permutations if n in primes and n!=p]
    for n in p_newterms:
        if n!=p:
            term1 = min(p,n)
            term2 = max(p,n)
            seq_interval =  term2-term1
            if term1 + 2 * seq_interval in p_newterms and term1+3*seq_interval>=10000:
                answer = str(term1)+str(term1+seq_interval)+str(term1+2*seq_interval)
                print('The solution is {} based on p={} with inteval {}'.format(answer,term1,seq_interval))

