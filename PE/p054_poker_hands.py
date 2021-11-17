"""
https://projecteuler.net/problem=54
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""

def ranking(hand: set) -> str:
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    all_are_same_suit = all([suit==suits[0] for suit in suits])
    values_are_consecutive = False
    values_are_royal = False  
    if all_are_same_suit and values_are_consecutive:
        if values_are_royal:
            return 'Royal Flush'
        elif values_are_consecutive:
            return 'Straight Flush'
    if True:
        return 'Four of a Kind'
    return 'High Card'

def p1_is_winner(p1_hand: set, p2_hand: set) -> bool:
    return True

p1_score = 0
counter = 0
filepath='p054_poker.txt'
with open(filepath) as fp:
    for line in fp:
        # if counter > 1:
        #     break
        line = line.strip("\n")
        cards = line.split(' ')
        p1_hand = set(cards[0:5])
        p2_hand = set(cards[5:10])
        # print('{} and {}'.format(p1_hand,p2_hand))a
        if p1_is_winner(p1_hand,p2_hand):
            p1_score+=1
        counter+=1
fp.close

print(p1_score)