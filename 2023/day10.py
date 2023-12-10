import os
import math
MAX_DISTANCE = 1000000
output1 = 0
output2 = 0
correctOutput = (6870, 0)
pipes = []
coordsMap = {}
coordsToProcess = []
class Coord:
    def __init__(self, x, y, pipe):
        self.x = x
        self.y = y
        self.pipe = pipe

def getNeighborCoords(pipes, coord, maxX, maxY):
    x = coord[0]
    y = coord[1]
    pipe = pipes[y][x]
    if pipe == 'S':
        neighbors = []
        if x > 0 and pipes[y][x-1] in ('-', 'L', 'F'):
            neighbors.append((x-1, y))
        if x < maxX and pipes[y][x+1] in ('-', 'J', '7'):
            neighbors.append((x+1, y))
        if y > 0 and pipes[y-1][x] in ('|', 'F', '7'):
            neighbors.append((x, y-1))
        if y < maxY and pipes[y+1][x] in ('|', 'L', 'J'):
            neighbors.append((x, y+1))
        return neighbors
    elif pipe == '|':
        return [(x, y-1), (x, y+1)]
    elif pipe == '-':
        return [(x-1, y), (x+1, y)]
    elif pipe == 'L':
        return [(x, y-1), (x+1, y)]
    elif pipe == 'J':
        return [(x, y-1), (x-1, y)]
    elif pipe == '7':
        return [(x, y+1), (x-1, y)]
    elif pipe == 'F':
        return [(x, y+1), (x+1, y)]
    else:
        print('UH OH')
        return []

def coordRepr(coord):
    return f'({coord[0]}, {coord[1]})'

input = open(os.path.join(os.getcwd(), "inputs/input10.txt"))
y = 0
for line in input:
    nextPipe = []
    for x, pipe in enumerate(list(line.strip())):
        if pipe == 'S':
            coordsToProcess.append(((x, y), 0))
            coordsMap.update({coordRepr((x, y)): 0})
        else:
            coordsMap.update({coordRepr((x, y)): MAX_DISTANCE}) #arbitrary max distance value
        nextPipe.append(pipe)
    pipes.append(nextPipe)
    y += 1
input.close()
maxX = len(pipes[0])
maxY = len(pipes)
# initial S pipe processing
(coord, distance) = coordsToProcess[0]
coordsToProcess = coordsToProcess[1:]
coordsToProcess.extend([(coord, distance+1) for coord in getNeighborCoords(pipes, coord, maxX, maxY)])
while len(coordsToProcess) > 0:
    # this is a queue
    (coord, distance) = coordsToProcess[0]
    coordsToProcess = coordsToProcess[1:]
    if distance < coordsMap[coordRepr(coord)]:
        coordsMap[coordRepr(coord)] = distance
        coordsToProcess.extend([(coord, distance+1) for coord in getNeighborCoords(pipes, coord, maxX, maxY)])
output1 = max(filter(lambda val: val != MAX_DISTANCE, coordsMap.values()))
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
# assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)