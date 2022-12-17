import os

input = open(os.path.join(os.getcwd(), "inputs/input14.txt"))
# coords is a dictionary of coordinates where the keys are y-values
# and values are sets of x-values that correspond to the y-value key
# note that higher y-values are lower in physical space
coords = {}
SAND_SOURCE = [500,0]

def addCoord(coord: [int]):
    """add the coordinate to our global dictionary of "filled" coordinates"""
    global coords
    if coord[1] in coords:
        coords[coord[1]].add(coord[0])
    else:
        coords[coord[1]] = set([coord[0]])
    return

def iterateAlongLine(c1: [int], c2: [int]):
    addCoord(c1)
    if c1[0] == c2[0]: #vertical line
        step = 1 if c1[1] < c2[1] else -1
        for y in range(c1[1] + step, c2[1], step):
            addCoord([c1[0], y])
    else: #horizontal line
        step = 1 if c1[0] < c2[0] else -1
        for x in range(c1[0] + step, c2[0], step):
            addCoord([x, c1[1]])
    addCoord(c2)
    return

def isEndless(coord: [int]) -> bool:
    """
    returns True if there is no sand blocking the path
    all the way down; False otherwise
    """
    global coords
    for y in sorted(coords, reverse=True):
        if y <= coord[1]:
            return True
        if inCoords([coord[0], y]):
            return False
    return True

def inCoords(coord: [int], floor: int = -1) -> bool:
    global coords
    x, y = coord
    return (floor > -1 and y == floor) or (y in coords and x in coords[y])

def getPath(coord: [int], floor: int = -1) -> [int]:
    """get the vector to move from this coord
    based on what cells are filled below it
    first checks immediately down, then down-left, then down-right
    if all spaces are taken, returns [0, 0] to indicate
    the unit of sand has come to a rest
    """
    global coords
    vectors = [[0, 1], [-1, 1], [1, 1]]
    for vector in vectors:
        if not inCoords([coord[0]+vector[0], coord[1]+vector[1]], floor):
            return vector
    return [0, 0]

def dropSand(coord: [int], floor: int = -1) -> bool:
    """returns True if sand should continue to drop, else false"""
    global SAND_SOURCE
    if floor == -1 and isEndless(coord):
        return False
    vector = getPath(coord, floor)
    if vector == [0, 0]:
        addCoord(coord)
        return floor == -1 or coord != SAND_SOURCE
    else:
        return dropSand([coord[0]+vector[0], coord[1]+vector[1]], floor)

for line in input.readlines():
    prevCoord = None
    for coord in line.strip().split(' -> '):
        currCoord = list(map(int, coord.split(',')))
        if not prevCoord == None:
            iterateAlongLine(prevCoord, currCoord)
        prevCoord = currCoord
input.close()

part1, part2 = 0, 0
while dropSand(SAND_SOURCE):
    part1 += 1
assert part1 == 715, f'Part 1: expected 715 but got {part1}'
print("part 1: ", part1)

part2 = part1 #continue dropping sand where we left off
maxFloor = max(coords.keys())+2
while dropSand(SAND_SOURCE, maxFloor):
    part2 += 1
# off by 1 since the while loop terminates before the final sand unit is counted
part2 += 1
assert part2 == 25248, f'Part 2: expected 25248 but got {part2}'
print("part 2: ", part2)