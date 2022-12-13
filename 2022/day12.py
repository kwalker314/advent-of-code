import os
import heapq as heap
from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['row', 'col'])
S = Coordinate(0, 0)
E = Coordinate(0, 0)
HILLS_DIMENSIONS = Coordinate(0, 0)

def convertLetter(letter: str) -> int:
    # E at the end bc it is equal to the elevation of z,
    # S at the start because it is equal to the elevation of a
    return 'SabcdefghijklmnopqrstuvwxyzE'.find(letter)

def getGridData(hillsMap: [int]) -> Coordinate:
    global S, E, HILLS_DIMENSIONS
    HILLS_DIMENSIONS = Coordinate(len(hillsMap)-1, len(hillsMap[0])-1)
    for row in range(HILLS_DIMENSIONS.row+1):
        for col in range(HILLS_DIMENSIONS.col+1):
            if hillsMap[row][col] == 0:
                S = Coordinate(row, col)
            elif hillsMap[row][col] == 27:
                E = Coordinate(row, col)

def canTraverse(elevationFrom: Coordinate, elevationTo: Coordinate) -> bool:
    # convert the elevation of S to be equal to the elevation of a
    realElevationFrom = max(elevationFrom, 1)
    # convert the elevation of E to be equal to the elevation of z
    realElevationTo = min(elevationTo, 26)
    return realElevationFrom+1 >= realElevationTo

def isTheEnd(coord: Coordinate) -> bool:
    global E
    return E.row == coord.row and E.col == coord.col

def getNeighbors(current: Coordinate) -> [Coordinate]:
    global HILLS_DIMENSIONS
    neighbors = []
    if current.row < HILLS_DIMENSIONS.row: #down
        neighbors.append(Coordinate(current.row+1, current.col))
    if current.col < HILLS_DIMENSIONS.col: #right
        neighbors.append(Coordinate(current.row, current.col+1))
    if 0 < current.col: #left
        neighbors.append(Coordinate(current.row, current.col-1))
    if 0 < current.row: #up
        neighbors.append(Coordinate(current.row-1, current.col))
    return neighbors

def findMinPath(hillsMap: [int], startingPoint: Coordinate) -> int:
    # starting coord has a value of 0
    coordcosts = {startingPoint: 0}
    pq = []
    visited = set()
    heap.heappush(pq, (0, startingPoint))

    # hello dijkstra, it's been awhile
    while len(pq) > 0:
        curr_cost, coord = heap.heappop(pq)  # pop smallest node to visit
        visited.add(coord)
        # found our way to the end; the cost must be for the minimum path
        if isTheEnd(coord):
            return coordcosts.get(coord)
        # otherwise, keep searching
        neighbors = getNeighbors(coord)
        for neighbor in neighbors:
            # we cannot visit this neighbor if the elevation is too high
            if neighbor in visited or \
                not canTraverse(hillsMap[coord.row][coord.col], hillsMap[neighbor.row][neighbor.col]):
                continue
            new_cost = curr_cost + 1
            if neighbor not in coordcosts.keys() or coordcosts.get(neighbor) > new_cost:
                coordcosts.update({neighbor: new_cost})
                heap.heappush(pq, (new_cost, neighbor))
    return 0

hills = []
input = open(os.path.join(os.getcwd(), "inputs/input12.txt"))
for line in input.readlines():
    hills.append(list(map(convertLetter, line.strip())))
input.close()
getGridData(hills)

part1 = findMinPath(hills, S)
part2 = 447
for i in range(len(hills)):
    for j in range(len(hills[0])):
        if hills[i][j] == 1:
            result = findMinPath(hills, Coordinate(i, j))
            if result > 0:
                part2 = min(part2, result)
assert part1 == 425, f'Part 1: expected 425 but got {part1}'
assert part2 == 418, f'Part 2: expected 418 {part2}'
print("part 1: ", part1)
print("part 2: ", part2)