"""
https://projecteuler.net/problem=54
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""

hand_ranking = ['High Card','One Pair','Two Pairs','Three of a Kind','Straight','Flush','Full House','Four of a Kind','Straight Flush','Royal Flush']
card_ranking = ['1','2','3','4','5','6','7','8','9','T','J','Q','K','A']

def ranking(hand: set) -> str:
    values = [card[0] for card in hand]
    values_numeric = set({card_ranking.index(value) for value in values})
    value_counts = [values.count(card) for card in values]
    suits = [card[1] for card in hand]
    all_are_same_suit = all([suit==suits[0] for suit in suits])
    values_are_consecutive = ( values_numeric == set({min(values_numeric) + i for i in range(5)}) ) #needs to handle aces !
    values_are_royal = (set(values)==set({'T','J','Q','K','A'}))  
    if all_are_same_suit and values_are_royal:
        return 'Royal Flush'
    if all_are_same_suit and values_are_consecutive:
        return 'Straight Flush'
    if 4 in value_counts:
        return 'Four of a Kind'
    if 3 in value_counts and 2 in value_counts:
        return 'Full House'
    if all_are_same_suit:
        return 'Flush'
    if values_are_consecutive:
        return 'Straight'
    if 3 in value_counts:
        return 'Three of a Kind'
    if value_counts.count(2)==2:
        return 'Two Pairs'
    if 2 in value_counts:
        return 'One Pair'
    return 'High Card'

def p1_is_winner(p1_hand: set, p2_hand: set) -> bool:
    p1_rank = ranking(p1_hand)
    p2_rank = ranking(p2_hand)
    if hand_ranking.index(p1_rank) > hand_ranking.index(p2_rank):
        return True
    if hand_ranking.index(p1_rank) < hand_ranking.index(p2_rank):
        return False
    #handle cases where they're equal
    
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
        # print('{} and {}'.format(p1_hand,p2_hand))
        if p1_is_winner(p1_hand,p2_hand):
            p1_score+=1
        counter+=1
fp.close

print(p1_score)