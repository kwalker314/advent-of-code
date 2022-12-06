import os
import sys
import re
import numpy as np

def replaceEmptySpaces(input: str) -> [str]:
    #4 spaces per crate stack column
    #today's puzzle challenge is formatting ig :^)
    return input.replace('    ', '[_] ').strip()

def formatStacks(stacks: [str]) -> [[str]]:
    #stacks come in in row order from top to bottom
    #so reverse them since that's how they'll be
    #processed anyway
    stacks.reverse()
    processedStacks = []
    for stackRow in stacks:
        letters = re.findall(r'[a-zA-Z_]', stackRow)
        processedStacks.append(letters)

    #use a jackhammer for this nail of an array vis a vis
    #numpy for easy array-axis-switching
    processedStacks = np.array(processedStacks)
    processedStacks = np.swapaxes(processedStacks, 0, 1)

    #andddd shove each row into a single string for final processing
    finalStacks = []
    for line in processedStacks:
        #aha! the underscore was a placeholder all along!
        newLine = ''.join(line).replace('_', '')
        #append an array of the same line twice since we
        #need to keep stack rows separate for parts 1 and 2
        finalStacks.append([newLine, newLine])
    return finalStacks

def processInput() -> ([str], [int]):
    input = open(os.path.join(os.getcwd(), "inputs/input05.txt"))
    stacks = []
    commands = []
    processingStacks = True
    for line in input:
        if line.find('[') == -1:
            #:( aoc days where input has multiple sections <<<<
            processingStacks = False
        if processingStacks:
            #processing stacks so replace empty spaces in the stacks
            stacks.append(line.replace('    ', '[_] ').strip())
        elif not processingStacks and line.find('move') > -1:
            #processing commands - save each line as an array of ints
            command = re.findall(r'\d+', line.strip())
            commands.append(list(map(int, command)))
    input.close()

    return (formatStacks(stacks), commands)

def processCommands(stacks: [str], commands: [[int]]) -> [str]:
    for command in commands:
        #get number of crates to move, the source stack for the crates,
        #and their destination stack (with -1 adjustment bc index numbers are
        #given in human and not computer)
        numCrates, srcStack, destStack = command[0], command[1]-1, command[2]-1

        #get crate string and reverse it for part 1
        cratesStr1 = stacks[srcStack][0][-numCrates:][::-1]
        #do the same for part 2 but without the reverse
        cratesStr2 = stacks[srcStack][1][-numCrates:]

        #remove required crates from the source stack
        stacks[srcStack][0] = stacks[srcStack][0][:-numCrates]
        stacks[srcStack][1] = stacks[srcStack][1][:-numCrates]

        #append the required crates to the destination stack
        stacks[destStack][0] = stacks[destStack][0] + cratesStr1
        stacks[destStack][1] = stacks[destStack][1] + cratesStr2
    return stacks

(stacks, commands) = processInput()
stacks = processCommands(stacks, commands)

part1 = ''.join([stack[0][-1] for stack in stacks])
part2 = ''.join([stack[1][-1] for stack in stacks])

assert part1 == 'MQTPGLLDN', f'Part 1: expected MQTPGLLDN but got {part1}'
assert part2 == 'LVZPSTTCZ', f'Part 2: expected LVZPSTTCZ but got {part2}'

print("part 1: ", part1)
print("part 2: ", part2)