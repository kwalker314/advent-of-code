import os
import re
NUMBERS = re.compile(r'^Card\s+([\d]+):\s+([\s\d]+)\s+\|\s+([\s\d]+)$')
input = open(os.path.join(os.getcwd(), "inputs/input04.txt"))
output1 = 0
output2 = 0
winningCards = {}
cardsProducedDict = {}
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
# for each card in the list, which we go through starting from the final card
# (which inherently produced no additional cards), add up the sum of all
# cards produced by this card (including itself) and memoize it in the
# cardsProducedDict under this cardNum's index
# (...this sounds like a YuGiOh card effect LOL)
while len(cardsToProcess) > 0:
    cardNum = cardsToProcess.pop()
    numCardsProduced = 1 #card counts itself as a card it produced
    for producedCardNum in winningCards[cardNum]:
        numCardsProduced += cardsProducedDict[producedCardNum]
    cardsProducedDict[cardNum] = numCardsProduced
# finally, go back through all the cards in our dictionary and add up their values
for winningCardNum in cardsProducedDict.keys():
    output2 += cardsProducedDict[winningCardNum]
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)