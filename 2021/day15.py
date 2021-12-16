import numpy as np
import heapq as heap

INPUT, GRID_I, GRID_J, GRID_I2, GRID_J2 = "inputs/input15.txt", 99, 99, 499, 499

def getNeighbors(current: (int, int)) -> [(int, int)]:
    neighbors = []
    i = current[0]
    j = current[1]
    down = (i+1, j)
    if i < GRID_I:
        neighbors.append(down)
    right = (i, j+1)
    if j < GRID_J:
        neighbors.append(right)
    left = (i, j-1)
    if j > 0:
        neighbors.append(left)
    up = (i-1, j)
    if i > 0:
        neighbors.append(up)
    return neighbors

def getNeighbors2(current: (int, int)) -> [(int, int)]:
    neighbors = []
    i = current[0]
    j = current[1]
    down = (i+1, j)
    if i < GRID_I2:
        neighbors.append(down)
    right = (i, j+1)
    if j < GRID_J2:
        neighbors.append(right)
    left = (i, j-1)
    if j > 0:
        neighbors.append(left)
    up = (i-1, j)
    if i > 0:
        neighbors.append(up)
    return neighbors

def part1(riskmap) -> int:
    riskmap[0][0] = 0
    pq = []
    visited = set()
    coordcosts = {}

    # starting coord has a value of 0
    coordcosts.update({(0, 0): 0})
    heap.heappush(pq, (0, (0, 0)))
    cost_1 = 0

    while len(pq) > 0:
        _, coord = heap.heappop(pq)  # pop smallest node to visit
        visited.add(coord)
        if coord == (GRID_I, GRID_J):
            cost_1 = coordcosts.get(coord)
            break
        neighbors = getNeighbors(coord)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            coord_cost = riskmap[neighbor[0]][neighbor[1]]
            new_cost = coordcosts.get(coord) + coord_cost
            if neighbor not in coordcosts.keys() or coordcosts.get(neighbor) > new_cost:
                coordcosts.update({neighbor: new_cost})
                heap.heappush(pq, (new_cost, neighbor))
    return cost_1

def part2(riskmap) -> int:
    riskmap2 = riskmap.copy()
    for i in range(1, 5): #horizontal tiling first: riskmap+(riskmap+1)+(riskmap+2)+(riskmap+3)+(riskmap+4)
        riskmap2 = np.concatenate((riskmap2, riskmap+i), axis=1)
    riskmap = riskmap2.copy()
    for i in range(1, 5): #the same as above but adding tiles vertically
        riskmap = np.concatenate((riskmap, riskmap2+i), axis=0)

    #don't forget to put values back below 10 after all the concatenations above
    for i in range(len(riskmap)):
        for j in range(len(riskmap[i])):
            val = riskmap[i][j]
            if 9 < val:
                riskmap[i][j] = val % 9

    riskmap[0][0] = 0
    pq = []
    visited = set()
    coordcosts = {}

    # starting coord has a value of 0
    coordcosts.update({(0, 0): 0})
    heap.heappush(pq, (0, (0, 0)))
    cost_2 = 0

    while len(pq) > 0:
        _, coord = heap.heappop(pq)  # pop smallest node to visit
        visited.add(coord)
        if coord == (GRID_I2, GRID_J2):
            cost_2 = coordcosts.get(coord)
            break
        neighbors = getNeighbors2(coord)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            coord_cost = riskmap[neighbor[0]][neighbor[1]]
            new_cost = coordcosts.get(coord) + coord_cost
            if neighbor not in coordcosts.keys() or coordcosts.get(neighbor) > new_cost:
                coordcosts.update({neighbor: new_cost})
                heap.heappush(pq, (new_cost, neighbor))

    return cost_2

if __name__ == '__main__':
    riskmap = np.genfromtxt(INPUT, dtype=np.int64, autostrip=True, delimiter=1)

    print(f'part 1: {part1(riskmap)}') #717
    print(f'part 2: {part2(riskmap)}') #2993