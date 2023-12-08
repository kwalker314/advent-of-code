import os
import re
import math
MAPPING_PATTERN = re.compile(r'^([A-Z]+)\s+=\s+\(([A-Z]+),\s+([A-Z]+)\)$')
START = "AAA"
END = "ZZZ"
output1 = 0
output2 = 0
correctOutput = (23147, 22289513667691)

def areAllGhostsGood(ghosts):
    for ghost in ghosts:
        if type(ghost) != int:
            return False
    return True

input = open(os.path.join(os.getcwd(), "inputs/input08.txt"))
dirs = input.readline().strip()
input.readline() # skip newline in input
mappings={}
for line in input:
    (source, destL, destR) = re.match(MAPPING_PATTERN, line.strip()).group(1, 2, 3)
    mappings[source]={"L": destL, "R": destR}
input.close()
index = 0
ghosts = [] #first ghostg is part 1 solution
ghosts.append('AAA')
for mapping in mappings.keys():
    if mapping != 'AAA' and mapping[-1] == 'A':
        ghosts.append(mapping)

# get the earliest point at which each ghost hits a 'Z';
# we'll get the LCM of all values at the end
while not areAllGhostsGood(ghosts):
    nextDir = dirs[index%(len(dirs))]
    for g, ghost in enumerate(ghosts):
        if type(ghost) != int:
            if ghost[-1] == 'Z':
                if g == 0 and ghost == 'ZZZ': #part 1 "ghost"
                    output1 = index
                ghosts[g] = index
            else:
                ghosts[g] = mappings[ghost][nextDir]
    index += 1
output2 = math.lcm(*ghosts) #damn this math minor is paying dividends (hah)
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)