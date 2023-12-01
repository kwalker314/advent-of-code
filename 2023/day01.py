import os
import sys
import re
textNumPattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))')
def getNum(strNum):
    if strNum == 'one' or strNum == '1':
        return 1
    elif strNum == 'two' or strNum == '2':
        return 2
    elif strNum == 'three' or strNum == '3':
        return 3
    elif strNum == 'four' or strNum == '4':
        return 4
    elif strNum == 'five' or strNum == '5':
        return 5
    elif strNum == 'six' or strNum == '6':
        return 6
    elif strNum == 'seven' or strNum == '7':
        return 7
    elif strNum == 'eight' or strNum == '8':
        return 8
    elif strNum == 'nine' or strNum == '9':
        return 9

input = open(os.path.join(os.getcwd(), "inputs/input01.txt"))
sums = (0,0)
correctSums = (55621, 53592) #53587 incorrect, 53592?
for line in input:
    matches1 = re.findall(r'\d', line)
    matches2 = re.findall(textNumPattern, line)
    print(matches2)
    sum0 = (10*int(matches1[0]) if len(matches1) > 0 else 0) + (int(matches1[-1]) if len(matches1) > 0 else 0)
    sum1 = (10*getNum(matches2[0]) if len(matches2) > 0 else 0) + (getNum(matches2[-1]) if len(matches2) > 0 else 0)
    sums=(sums[0]+sum0, sums[1]+sum1)
input.close()
# assert sums[0] == correctSums[0], f'Part 1: expected {correctSums[0]} but got {sums[0]}'
# assert sums[1] == correctSums[1], f'Part 2: expected {correctSums[1]} but got {sums[1]}'
print("part 1: ", sums[0])
print("part 2: ", sums[1])
