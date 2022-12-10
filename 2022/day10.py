import os

X_VAR = 1
CYCLE = 0
X_SUM = 0
CRT_DISPLAY = [['.']*40 for i in range(6)]

def getCommands() -> [[str, int]]:
    commands = []
    input = open(os.path.join(os.getcwd(), "inputs/input10.txt"))
    for line in input.readlines():
        command = line.strip().split(' ')
        if command[0] == 'noop':
            command = ['noop', 0]
        else:
            command[1] = int(command[1])
        commands.append(command)
    input.close()
    return commands

def drawPixel(cycle: int, x_var: int):
    global CRT_DISPLAY
    if x_var-1 <= (cycle%40) <= x_var+1:
        CRT_DISPLAY[(cycle)//40][(cycle)%40] = '#'
    return

def checkCycle():
    global CYCLE
    global X_VAR
    global X_SUM
    CYCLE += 1
    if (CYCLE-20)%40 == 0:
        X_SUM += (X_VAR*CYCLE)
    drawPixel(CYCLE-1, X_VAR)
    return

def processCommand(command: [str, int]):
    global X_VAR
    checkCycle()
    if command[0] == 'addx':
        checkCycle()
        X_VAR += command[1]
    return

for command in getCommands():
    processCommand(command)

part1 = X_SUM
part2 = ''
for line in CRT_DISPLAY:
    part2 += '\n' + ''.join(line)

part2Assert = \
    '\n####..##..#....#..#.###..#....####...##.' + \
    '\n#....#..#.#....#..#.#..#.#....#.......#.' + \
    '\n###..#....#....####.###..#....###.....#.' + \
    '\n#....#.##.#....#..#.#..#.#....#.......#.' + \
    '\n#....#..#.#....#..#.#..#.#....#....#..#.' + \
    '\n####..###.####.#..#.###..####.#.....##..'
assert part1 == 13920, f'Part 1: expected 13920 but got {part1}'
assert part2 == part2Assert, f'Part 2: expected {part2Assert} \n but got \n {part2}'
print("part 1: ", part1)
print("part 2: ", part2) # EGLHBLFJ