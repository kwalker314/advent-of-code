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
print("part 1: ", sums[0])
print("part 2: ", sum(sums[0:3]))
