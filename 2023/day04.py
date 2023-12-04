import os
import re
NUMBERS = re.compile(r'^Card\s+([\d]+):\s+([\s\d]+)\s+\|\s+([\s\d]+)$')
input = open(os.path.join(os.getcwd(), "inputs/input04.txt"))
output1 = 0
output2 = 0
winningCards = {}
correctOutput = (20829, 12648035)
cardsToProcess = []
for line in input:
    pointVal = 0
    parsed = re.match(NUMBERS, line.strip())
    (cardNum, yourNums, winningNums) = parsed.group(1, 2, 3)
    cardNum = int(cardNum)
    yourNums = yourNums.strip().replace('  ', ' ').split(' ')
    winningNums = winningNums.strip().replace('  ', ' ').split(' ')
    numWins = 0
    for yourNum in yourNums:
        if yourNum in winningNums:
            numWins += 1
            pointVal = pointVal*2 if pointVal > 0 else 1
    winningCards[cardNum] = [x for x in range(cardNum+1,cardNum+numWins+1)]
    output1 += pointVal
    cardsToProcess.append(cardNum)
input.close()
while len(cardsToProcess) > 0:
    cardNum = cardsToProcess.pop()
    output2 += 1
    cardsToProcess.extend(winningCards[cardNum])
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)