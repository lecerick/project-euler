"""
Problem 22
---------------
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
import io

char_value = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def isEarlier(s1: str, s2: str):
    """ Returns True if s1 comes earlier in alphabetical order than s2. E.g. isEarlier('Mary','Sue') would return True"""
    if s1 == s2:
        return False
    for i in range(0,min(len(s1),len(s2))):
        s1v =char_value[s1[i]]
        s2v =char_value[s2[i]]
        # print('{}({}) versus {}({})'.format(s1[i],s1v,s2[i],s2v))
        if s1v < s2v:
            return True
        if s1v > s2v:
            return False
    if len(s1)<len(s2):
        return True
    else:
        return False

with open('p022_names.txt','r') as fp:
    names = fp.readline().replace("\"","").split(",")
fp.close()
  
sorted_names = sorted(names)

total_score = 0
for i in range(0,len(sorted_names)):
    position = i +1
    name = sorted_names[i]
    score = 0
    for j in range(0,len(name)):
        score+=char_value[name[j]]
    score*=position
    if name == 'COLIN':
        print('{} is name #{} with a score of {}'.format(name,position,score))
    total_score+=score

print('Total Score: {}'.format(total_score))