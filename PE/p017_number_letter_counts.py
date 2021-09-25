"""
Problem #17
----------------
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def wordyNum(n: int):
    """Takes any integer from 0 to 1000 and returns a string of its in written English equivalent (according to British usage)"""
    ones = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    tens = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    teens = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    if n == 0:
        return 'zero'
    if n < 10:
        return ones[n]
    if n < 100:
        if n%10 == 0:
            return tens[n//10]
        elif n//10 == 1:
            return teens[n]
        else:
            return tens[n//10] +'-'+ ones[n%10]
    if n<1000:
        if n % 100 == 0:
            return ones[n//100]+' hundred'
        else:
            return ones[n//100]+' hundred and '+ wordyNum(n%100)
    return 'one thousand'

def wordyCount(s: str):
    count = 0
    for i in range(0, len(s)):
        if s[i]!=' ' and s[i]!='-':
            count+=1
    return count

count = 0
for i in range(1,1001):
    count+=wordyCount(wordyNum(i))
print(count)