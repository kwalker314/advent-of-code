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

if __name__ == '__main__':
    riskmap = np.genfromtxt(INPUT, dtype=int, autostrip=True, delimiter=1)

    print(f'part 1: {part1(riskmap)}') #717
    print(f'part 2: {0}') #