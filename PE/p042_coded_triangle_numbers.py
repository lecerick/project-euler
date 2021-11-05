"""
Problem #42
------------
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using the input 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

with open('p042_words.txt','r') as fp:
    words = [word.strip("\"") for word in fp.readline().split(',')]
fp.close()

alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
triangle_numbers = set({i*(i+1)//2 for i in range(1,10**6)})
triangle_words = set({})
for word in words:
    word_value = sum([alphabet.index(char) for char in word])
    if word_value in triangle_numbers:
        triangle_words.add(word)

print(len(triangle_words))