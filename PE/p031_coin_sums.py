"""
Problem 31
---------------------------------
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

def coinSum():
    count = 1
    for x100 in range(0,3):
        sum= x100*100
        # print(sum)
        for x050 in range(0,(200-sum)//50+1):
            sum= x100*100 +x050*50
            for x020 in range(0,(200-sum)//20+1):
                sum= x100*100 +x050*50 + x020*20
                for x010 in range(0,(200-sum)//10+1):
                    sum= x100*100 +x050*50 + x020*20 + x010*10
                    for x005 in range(0,(200-sum)//5+1):
                        sum= x100*100 +x050*50 + x020*20 + x010*10 + x005*5
                        for x002 in range(0,(200-sum)//2+1):
                            sum= x100*100 +x050*50 + x020*20 + x010*10 + x005*5+ x002*2
                            x001 = max(200-sum,0)
                            sum+= x001*1
                            if sum==200:
                                print([x100,x050,x020,x010,x005,x002,x001])
                                count+=1
    return(count)

print(coinSum())