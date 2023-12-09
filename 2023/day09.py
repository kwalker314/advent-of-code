import os
import re
import math
output1 = 0
output2 = 0
correctOutput = (1666172641, 933)

def getNextVal(nums):
    allZeros = True
    nextNums = []
    for index, num in enumerate(nums):
        if allZeros and num != 0:
            allZeros = False
        if index > 0:
            nextNums.append(nums[index]-nums[index-1])
    if allZeros:
        return 0
    else:
        return nums[-1]+getNextVal(nextNums)

input = open(os.path.join(os.getcwd(), "inputs/input09.txt"))
for line in input:
    nums = [int(x) for x in line.strip().split(' ')]
    output1 += getNextVal(nums)
    nums.reverse()
    output2 += getNextVal(nums)

input.close()
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)