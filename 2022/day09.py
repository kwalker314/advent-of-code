import os

commands = []

# heads is coords[0], tails are coords[1-9]
coords = [[0, 0] for x in range(10)]
visited = [set(tuple()), set(tuple())]

def getCommands():
    input = open(os.path.join(os.getcwd(), "inputs/input09.txt"))
    for line in input.readlines():
        command = line.strip().split(' ')
        command[1] = int(command[1])
        commands.append(command)
    input.close()
    return

def processU(distance: int):
    coords[0][1] -= distance
    return

def processD(distance: int):
    coords[0][1] += distance
    return

def processL(distance: int):
    coords[0][0] -= distance
    return

def processR(distance: int):
    coords[0][0] += distance
    return

def tailInRange(tailIndex: int = 1) -> bool:
    """
    check if the tail is close enough to its relevant neighbor
    (within one space vertically and/or horizontally - diagonals are ok)
    and add its current coordinates to the relevant visited set
    """
    if tailIndex == 1:
        visited[0].add(tuple(coords[1]))
    elif tailIndex == 9:
        visited[1].add(tuple(coords[9]))
    return abs(coords[tailIndex][0] - coords[tailIndex-1][0]) < 2 and \
        abs(coords[tailIndex][1] - coords[tailIndex-1][1]) < 2

def moveHorizontally(tailIndex: int = 1):
    dx = coords[tailIndex-1][0] - coords[tailIndex][0]
    dx = dx/abs(dx)
    coords[tailIndex][0] += int(dx)
    return

def moveVertically(tailIndex: int = 1):
    dy = coords[tailIndex-1][1] - coords[tailIndex][1]
    dy = dy/abs(dy)
    coords[tailIndex][1] += int(dy)
    return

def moveDiagonally(tailIndex: int = 1):
    moveHorizontally(tailIndex)
    moveVertically(tailIndex)
    return

def moveTowardsHead(tailIndex: int = 1):
    if coords[tailIndex][0] == coords[tailIndex-1][0]:
        moveVertically(tailIndex)
    else: #coords[tailIndex][1] == coords[tailIndex-1][1]
        moveHorizontally(tailIndex)
    return

def moveTail(tailIndex: int = 1):
    # diagonal movement
    if coords[tailIndex][0] != coords[tailIndex-1][0] and \
        coords[tailIndex][1] != coords[tailIndex-1][1]:
        moveDiagonally(tailIndex)
    else: # horizontal/vertical-only movement
        moveTowardsHead(tailIndex)
    return

def processCommand(command: str):
    if command[0] == 'U':
        processU(command[1])
    elif command[0] == 'D':
        processD(command[1])
    elif command[0] == 'R':
        processR(command[1])
    elif command[0] == 'L':
        processL(command[1])
    
    for tailIndex in range(1, len(coords)):
        while not tailInRange(tailIndex):
            moveTail(tailIndex)
            movedTail = True
    return

getCommands()

for command in commands:
    processCommand(command)

part1, part2 = len(visited[0]), len(visited[1])

# assert part1 == 6181, f'Part 1: expected 6181 but got {part1}'
# assert part2 == '', f'Part 2: expected sdkfjlsdkjf but got {part2}'
# 2376, 2377 too low
print("part 1: ", part1)
print("part 2: ", part2)