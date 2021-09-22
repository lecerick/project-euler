"""
Problem #15
-------------
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?1
"""
pascalsTriangle = [[1],[1,2,1]]

for i in range(2,50):
    row = [1]
    for j in range(1, len(pascalsTriangle[i-1])):
        n1 =int(pascalsTriangle[i-1][j])
        n2 =int(pascalsTriangle[i-1][j-1])
        row.append(n1+n2)
    row.append(1)
    # print(row)
    pascalsTriangle.append(row)

print('Solution to 2x2: '+str(max(pascalsTriangle[2+2-1])))
print('Solution to 3x3: '+str(max(pascalsTriangle[3+3-1])))
print('Solution to 10x10: '+str(max(pascalsTriangle[10+10-1])))
print('Solution to 20x20: '+str(max(pascalsTriangle[20+20-1])))