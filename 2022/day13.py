import os
import ast

def compareGroup(sideA, sideB) -> int:
    """
    returns -1 if the sides are in the correct order, 0
    if it's too early to tell, and 1 if the sides are in the incorrect order
    if sideA and sideB are both ints, return sideA - sideB
    """
    if isinstance(sideA, int) and isinstance(sideB, int):
        return (sideA - sideB)/abs(sideA - sideB) if sideB != sideA else 0
    elif isinstance(sideA, int) and isinstance(sideB, list):
        return compareGroup([sideA], sideB)
    elif isinstance(sideA, list) and isinstance(sideB, int):
        return compareGroup(sideA, [sideB])
    else: # sideA and sideB are both of type list
        for i in range(len(sideA)): 
            if i >= len(sideB): # sideB is out of list items
                return 1
            compResult = compareGroup(sideA[i], sideB[i])
            if compResult != 0:
                return compResult
            else:
                continue
        # if we get to this point, the lists are identical
        # so we can't know whether the parent list is in the
        # correct order yet
        return -1 if len(sideA) < len(sideB) else 0

input = open(os.path.join(os.getcwd(), "inputs/input13.txt"))
groups = []
for group in input.read().split('\n\n'):
    # truly a disgusting number of parentheses on the following line
    groups.append(list(map(ast.literal_eval, group.strip().split('\n'))))
input.close()

part1, part2 = 0, 0
index = 1
for group in groups:
    print(f'index: {index}')
    if compareGroup(group[0], group[1]) < 1:
        # print(f'{group[0]} is before {group[1]}')
        part1 += index
    # else:
        # print(f'{group[0]} is NOT before {group[1]}')
    index += 1

assert part1 == 5330, f'Part 1: expected 5330 but got {part1}'
# assert part2 == 418, f'Part 2: expected 418 {part2}'
print("part 1: ", part1)
print("part 2: ", part2)