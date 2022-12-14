import os
import ast
import functools

def compareGroup(sideA, sideB) -> int:
    """
    returns -1 if the sides are in the correct order, 0 if it's
    too early to tell, and 1 if the sides are in the incorrect order
    
    if sideA and sideB are both ints, return according to the
    above return values for ascending order

    if one of sideA and sideB is a list but the other is an int,
    convert the non-list one to an int and re-compare

    if both sideA and sideB are lists, compare their elements
    one by one recursively - in the event of each element
    being equal, returns -1 if sideA has fewer items, 1 if
    sideB has fewer items, and 0 if they're the same length
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
for line in input.readlines():
    lineStripped = line.strip()
    if len(lineStripped) > 0:
        groups.append(ast.literal_eval(lineStripped))
input.close()

# initialize part2 to 1 bc we're gonna have to multiply for part 2
part1, part2 = 0, 1
for i in range(0, len(groups), 2):
    if compareGroup(groups[i], groups[i+1]) < 1:
        part1 += int(i/2)+1

# add the necessary list items, then sort
# using our ~handy dandy~ comparison function written for part 1
groups += [[[2]], [[6]]]
groups.sort(key=functools.cmp_to_key(compareGroup))

# find where the list items we added ended up and
# multiply the indices of each (where indexes start at ONE,
# for some reason) together for part 2's answer!
for i in range(len(groups)):
    if groups[i] in [[[2]], [[6]]]:
        part2 *= i+1

assert part1 == 5330, f'Part 1: expected 5330 but got {part1}'
assert part2 == 27648, f'Part 2: expected 27648 {part2}'
print("part 1: ", part1)
print("part 2: ", part2)