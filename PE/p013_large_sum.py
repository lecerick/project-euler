"""
Work out the first ten digits of the sum of one-hundred 50-digit numbers.
"""
import io

def generateList(filepath: str):
    nums = []
    f = open(filepath)
    while True:
        n = f.read(50)
        if n == '':
            break
        nums.append(int(n))
        f.read(1)
    f.close()
    return nums

def firstTenDigits(nums: list):
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
    s = str(sum)
    firstTen = s[0:10]
    return int(firstTen)

input = generateList('PE\p013_input.txt')
print(firstTenDigits(input))