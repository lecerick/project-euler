"""
Problem 31
---------------------------------
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coin_value = [200,100,50,20,10,5,2,1]
coin_combo = [1,0,0,0,0,0,0,0]
ways_of_making_change = [coin_combo]
# print(sum([a*b for a,b in zip(coin_value,coin_combo)]))

def exchange(coins):
    smallest_exchangable=6
    while coins[smallest_exchangable]==0:
        smallest_exchangable-=1
    exchanged_value = coin_value[smallest_exchangable]
    coins[smallest_exchangable]-=1
    coins[smallest_exchangable+1]+= exchanged_value // coin_value[smallest_exchangable+1]
    remains = exchanged_value % coin_value[smallest_exchangable+1]
    if smallest_exchangable!=6:
        coins[smallest_exchangable+2]+= remains // coin_value[smallest_exchangable+2]
    return coins

count = 1
print('Combo #{}: {} worth {}'.format(count,coin_combo,sum([a*b for a,b in zip(coin_value,coin_combo)])))

while coin_combo!=[0, 0, 0, 0, 0, 0, 0, 200]:
    coin_combo = exchange(coin_combo)
    count+=1
    print('Combo #{}: {} worth {}'.format(count,coin_combo,sum([a*b for a,b in zip(coin_value,coin_combo)])))


print(count)
# print(ways_of_making_change)
# print(len(ways_of_making_change))