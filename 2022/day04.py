import os
import sys

def parseRanges(ranges: str) -> (str, str):
    ranges = ranges.split(',')
    return (ranges[0], ranges[1])

def parseRange(range: str) -> (int, int):
    splitRange = range.split('-')
    return int(splitRange[0]), int(splitRange[1])

def checkContainsAndOverlap(range1: str, range2: str) -> (bool, bool):
    range1Start, range1End = parseRange(range1)
    range2Start, range2End = parseRange(range2)
    rangeContained = (range1Start <= range2Start and range1End >= range2End) \
        or (range2Start <= range1Start and range2End >= range1End)
    #ty stackoverflow for this ez range overlap check!
    rangeOverlap = max(range1Start, range2Start) <= min(range1End, range2End)
    return (rangeContained, rangeOverlap)

def checkRanges(line: str) -> (bool, bool):
    range1, range2 = parseRanges(line)
    return checkContainsAndOverlap(range1, range2)

input = open(os.path.join(os.getcwd(), "inputs/input04.txt"))
part1 = 0
part2 = 0
for line in input:
    results = checkRanges(line.strip())
    part1 += results[0]
    part2 += results[1]
input.close()
assert part1 == 513, f'Part 1: expected 513 but got {part1}'
assert part2 == 878, f'Part 2: expected 878 but got {part2}'
print("part 1: ", part1)
print("part 2: ", part2)
