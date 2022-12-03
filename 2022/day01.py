import os
import sys

input = open(os.path.join(os.getcwd(), "inputs/input01.txt"))
sums = []
currSum = 0
for line in input:
    if line == "\n":
        sums.append(currSum)
        currSum = 0
    else:
        currSum += int(line)
input.close()
sums.sort(reverse=True)
assert sums[0] == 71934, f'Part 1: expected 71934 but got {sums[0]}'
assert sum(sums[0:3]) == 211447, f'Part 2: expected 211447 but got {sum(sums[0:3])}'
print("part 1: ", sums[0])
print("part 2: ", sum(sums[0:3]))
