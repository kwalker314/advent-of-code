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
    def __init__(self, minVal, maxVal, diff):
        self.minVal = minVal
        self.maxVal = maxVal
        self.diff = diff
    def __repr__(self):
        return f'Breakpoint(minVal: {self.minVal}, maxVal: {self.maxVal}, diff: {self.diff})'

class ComplexSeed:
    def __init__(self, minVal, maxVal):
        self.minVal = minVal
        self.maxVal = maxVal
    def __repr__(self):
        return f'ComplexSeed(minVal: {self.minVal}, maxVal: {self.maxVal})'
    def overlaps(self, breakpoint: Breakpoint):
        return max(self.minVal, breakpoint.minVal) <= min(self.maxVal, breakpoint.maxVal)
    def contains(self, val):
        return self.minVal <= val <= self.maxVal

def splitComplexSeed(seed: ComplexSeed, breakpoint: Breakpoint):
    '''Returns ComplexSeed(s) according to the breakpoint: add the breakpoint's
    diff to the min/maxVals of the given seed and return other seed(s) with min/maxVals
    that fall outside the breakpoint's range.
    First value returned in the tuple is the list of seeds to add back to our queue
    (after the current breakpoint has been processed) because they have not been
    "mapped" yet;
    Second value is seeds that have already been "mapped" and can therefore be
    left alone for the rest of this mapping pass'''
    tempQueueSeeds = []
    tempProcessedSeeds = []
    containsMinVal = seed.contains(breakpoint.minVal)
    containsMaxVal = seed.contains(breakpoint.maxVal)
    # seed entirely contains breakpoint
    if containsMinVal and containsMaxVal:
        tempProcessedSeeds.append(ComplexSeed(breakpoint.minVal+breakpoint.diff,
            breakpoint.maxVal+breakpoint.diff))
        tempQueueSeeds.append(ComplexSeed(seed.minVal, breakpoint.minVal-1))
        tempQueueSeeds.append(ComplexSeed(breakpoint.maxVal+1, seed.maxVal))
    # breakpoint entirely contains seed
    elif max(seed.minVal, breakpoint.minVal) == seed.minVal and \
            min(seed.maxVal, breakpoint.maxVal) == seed.maxVal:
        tempProcessedSeeds.append(ComplexSeed(seed.minVal+breakpoint.diff, seed.maxVal+breakpoint.diff))
    elif containsMinVal: # seed does NOT contain breakpoint.maxVal
        tempProcessedSeeds.append(ComplexSeed(breakpoint.minVal+breakpoint.diff, seed.maxVal+breakpoint.diff))
        tempQueueSeeds.append(ComplexSeed(seed.minVal, breakpoint.minVal-1))
    elif containsMaxVal: # seed does NOT contain breakpoint.maxVal
        tempProcessedSeeds.append(ComplexSeed(seed.minVal+breakpoint.diff, breakpoint.maxVal+breakpoint.diff))
        tempQueueSeeds.append(ComplexSeed(breakpoint.maxVal+1, seed.maxVal))
    return (tempQueueSeeds, tempProcessedSeeds)

output1 = 0
output2 = 0
correctOutput = (261668924, 24261545)
input = open(os.path.join(os.getcwd(), "inputs/input05.txt"))
seedVals = re.match(SEED_VALS_PATTERN, input.readline().strip())[1].split(' ')
simpleSeeds = [Seed(int(s)) for s in seedVals]
cSeedsQueue = [ComplexSeed(int(s), int(s) + int(t)-1) for s, t in zip(seedVals[::2], seedVals[1::2])]
processedSeeds = [] # seeds that have been mapped - should not be reprocessed until the next mapping pass
deferredSeeds = [] # temp list for seeds that haven't been mapped but don't overlap with the current breakpoint
for line in input:
    # about to start next round of conversions so reset processed state of all
    # simpleSeeds and add seeds that were processed last pass to cSeedsQueue
    # to begin the next round of mapping
    if line.strip() == '' or re.match(MAP_HEADER_PATTERN, line.strip()) is not None:
        for seed in simpleSeeds:
            seed.processed = False
        cSeedsQueue.extend(processedSeeds)
        processedSeeds.clear()
        continue
    
    (destStart, sourceStart, rangeLen) = [int(s) for s in re.match(MAP_DETAILS_PATTERN, line.strip()).group(1, 2, 3)]
    rangeList = range(sourceStart, sourceStart+rangeLen)
    for seed in simpleSeeds:
        if not seed.processed and seed.val in rangeList:
            diff = seed.val-sourceStart
            seed.val = (destStart+diff)
            seed.processed = True
    breakpoint = Breakpoint(sourceStart, sourceStart+rangeLen-1, destStart-sourceStart)
    while len(cSeedsQueue) > 0:
        seed = cSeedsQueue.pop()
        if seed.overlaps(breakpoint):
            newQueueSeeds, newProcessedSeeds = splitComplexSeed(seed, breakpoint)
            # deferredSeeds don't get immediately re-added to cSeedsQueue bc we know they
            # don't overlap with the current loop breakpoint so no need to check them again
            deferredSeeds.extend(newQueueSeeds)
            processedSeeds.extend(newProcessedSeeds)
        else:
            # seed didn't overlap with this breakpoint so revisit it with the next breakpoint
            deferredSeeds.append(seed)
    cSeedsQueue.extend(deferredSeeds)
    deferredSeeds.clear()

input.close()
cSeedsQueue.extend(processedSeeds)
output1 = min(map(lambda seed: seed.val, simpleSeeds))
output2 = min(map(lambda seed: seed.minVal, cSeedsQueue))
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)