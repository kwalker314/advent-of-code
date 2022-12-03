import os
import sys

PRIORITY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def splitMatch(rucksack: str) -> str:
    half1, half2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return set(half1).intersection(half2).pop()

def tripleMatch(rs1: str, rs2: str, rs3: str) -> str:
    return set(rs1).intersection(rs2).intersection(rs3).pop()

def getSplitPriority(rucksack: str) -> int:
    commonLetter = splitMatch(rucksack)
    return PRIORITY.find(commonLetter)+1

def getTripletPriority(rs1: str, rs2: str, rs3: str) -> int:
    commonLetter = tripleMatch(rs1, rs2, rs3)
    return PRIORITY.find(commonLetter)+1

input = open(os.path.join(os.getcwd(), "inputs/input03.txt"))
part1 = 0
part2 = 0
triplets = []
for line in input:
    part1 += getSplitPriority(line.strip())
    triplets.append(line.strip())
    if len(triplets) == 3:
        part2 += getTripletPriority(triplets[0], triplets[1], triplets[2])
        triplets.clear()
input.close()
assert part1 == 7785, f'Part 1: expected 7785 but got {part1}'
assert part2 == 2633, f'Part 2: expected 2633 but got {part2}'
print("part 1: ", part1)
print("part 2: ", part2)
