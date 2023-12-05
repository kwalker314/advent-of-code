import os
import re
SEED_VALS_PATTERN = re.compile(r'^seeds:\s+(.*)$')
MAP_HEADER_PATTERN = re.compile(r'^[a-z\-]+\smap:$')
MAP_DETAILS_PATTERN = re.compile(r'^(\d+) (\d+) (\d+)$')
class Seed:
    def __init__(self, val):
        self.val = val
        self.processed = False
    def __repr__(self):
        return f'Seed(val: {self.val}, processed: {self.processed})'

#we can assume that breakpoint min/maxes can't contain other breakpoints
class Breakpoint:
    def __init__(self, val, addVal):
        self.val = val
        self.addVal = addVal
    def __repr__(self):
        return f'Breakpoint(val: {self.val}, addVal: {self.addVal})'

class ComplexSeed:
    breakpoints = []
    def __init__(self, minVal, lenVal, addVal=0):
        self.minVal = minVal
        self.maxVal = minVal+lenVal
        self.addVal = addVal
    def __repr__(self):
        return f'ComplexSeed(minVal: {self.minVal}, maxVal: {self.maxVal}, addVal: {self.addVal}, breakpoints: {self.breakpoints})'
    def addBreakpoint(self, breakpoint):
        self.breakpoints.append(breakpoint)
    def contains(self, startVal, lenVal):
        return max(self.minVal, startVal) <= min(self.maxVal, startVal+lenVal)

def splitComplexSeeds(complexSeeds):
    '''Will need to iterate through each seed's breakpoints and create new ComplexSeed objects
    with the appropriate addVals
    '''
    for seed in complexSeeds:
        print(seed)
    return complexSeeds

output1 = 0
output2 = 0
correctOutput = (261668924, 0)
input = open(os.path.join(os.getcwd(), "inputs/input05.txt"))
seedVals = re.match(SEED_VALS_PATTERN, input.readline().strip())[1].split(' ')
simpleSeeds = [Seed(int(s)) for s in seedVals]
complexSeeds = [ComplexSeed(int(s), int(t)) for s, t in zip(*[iter(seedVals)]*2)]
for line in input:
    # about to start next round of conversions
    if line.strip() == '' or re.match(MAP_HEADER_PATTERN, line.strip()) is not None:
        print('next batch:',simpleSeeds)
        # reset processed state of all simpleSeeds for this mapping set
        # note that we don't need to care about simpleSeeds that we don't
        # find a map "match" for as they map to their same value
        for seed in simpleSeeds:
            seed.processed = False
        # complexSeeds = splitComplexSeeds(complexSeeds)
        continue
    
    (destStart, sourceStart, rangeLen) = [int(s) for s in re.match(MAP_DETAILS_PATTERN, line.strip()).group(1, 2, 3)]
    print('sourceStart, destStart, rangeLen:', sourceStart, destStart, rangeLen)
    rangeList = range(sourceStart, sourceStart+rangeLen+1)
    for seed in simpleSeeds:
        if not seed.processed and seed.val in rangeList:
            diff = seed.val-sourceStart
            seed.val = (destStart+diff)
            seed.processed = True
    # for seed in complexSeeds:
    #     if seed.contains(sourceStart, rangelen):
    #         # TODO: figure out what breakpoint(s) to add to the ComplexSeed along with the addVal (=rangeLen)
    #         print(seed)
input.close()
print(simpleSeeds)
for seed in simpleSeeds:
    output1 = seed.val if output1 == 0 else min(output1, seed.val)
# assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
# assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)