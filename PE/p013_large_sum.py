"""
Work out the first ten digits of the sum of one-hundred 50-digit numbers.
"""
import io

#perform io on txt file to create a list of 50-digit numbers
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
    # print(nums)
    return nums

#function to sum... is it possible to look at just the first 10 digits and infer whether it will round up?
def firstTenDigits(nums: list):
    sum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
    s = str(sum)
    firstTen = s[0:10]
    return int(firstTen)

input = generateList('p013_input.txt')
print(firstTenDigits(input))