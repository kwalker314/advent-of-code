import os
import re
LIMITS = (12, 13, 14) # red, green, blue color limits
PATTERN = re.compile(r'^Game (\d+): (.*)$')

def getGameOutput(bagOutput, minimums):
    number, color = bagOutput.split(' ')
    number = int(number)
    if color == 'red':
        return (int(number) <= LIMITS[0],
            (max(number, minimums[0]), minimums[1], minimums[2]))
    elif color == 'green':
        return (int(number) <= LIMITS[1],
            (minimums[0], max(number, minimums[1]), minimums[2]))
    elif color == 'blue':
        return (int(number) <= LIMITS[2],
            (minimums[0], minimums[1], max(number, minimums[2])))
    return False #shouldn't ever get here but juuuust in case

input = open(os.path.join(os.getcwd(), "inputs/input02.txt"))
outputs = (0,0)
correctOutput = (2176, 63700)

for line in input:
    matches = re.search(PATTERN,line)
    gameId, bagOutputs = int(matches[1]), matches[2]
    isGamePossible = True
    minimums = (0,0,0)
    for bagOutput in bagOutputs.split('; '):
        for singularOutput in bagOutput.split(', '):
            gameOutput, minimums = getGameOutput(singularOutput, minimums)
            #don't let a gameOutput result of True reset isGamePossible to True
            #if it was False from a previous result for this line
            isGamePossible = isGamePossible and gameOutput
    # part 1: add up all ids of games that are possible with the limits
    # part 2: multiply the rgb minimums of this game together and add them to the running total
    outputs = (outputs[0] + (gameId if isGamePossible else 0),
        outputs[1] + minimums[0]*minimums[1]*minimums[2])
input.close()

assert outputs[0] == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {outputs[0]}'
assert outputs[1] == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {outputs[1]}'
print("part 1: ", outputs[0])
print("part 2: ", outputs[1])