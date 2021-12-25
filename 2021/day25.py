F = "inputs/input25.txt"

def part2():
    return


def move_east(cucumbers: [str], movements: [(int, int)]) -> [str]:
    for movement in movements:
        i, j = movement
        new_j = 0 if j == len(cucumbers[i])-1 else j+1
        cucumbers[i][j], cucumbers[i][new_j] = cucumbers[i][new_j], cucumbers[i][j]
    return cucumbers

def step_east(cucumbers: [str]) -> (bool, [str]):
    moved = False
    move_coords = []
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[i])):
            if cucumbers[i][j] != '>':
                continue
            new_loc = 0 if j == len(cucumbers[i])-1 else j+1
            if cucumbers[i][new_loc] == '.':
                moved = True
                move_coords.append((i, j))
    return moved, move_east(cucumbers, move_coords)


def move_south(cucumbers: [str], movements: [(int, int)]) -> [str]:
    for movement in movements:
        i, j = movement
        new_i = 0 if i == len(cucumbers)-1 else i+1
        cucumbers[i][j], cucumbers[new_i][j] = cucumbers[new_i][j], cucumbers[i][j]
    return cucumbers


def step_south(cucumbers: [str]) -> (bool, [(int, int)]):
    moved = False
    move_coords = []
    for i in range(len(cucumbers)):
        for j in range(len(cucumbers[i])):
            if cucumbers[i][j] != 'v':
                continue
            new_loc = 0 if i == len(cucumbers)-1 else i+1
            if cucumbers[new_loc][j] == '.':
                moved = True
                move_coords.append((i, j))
    return moved, move_south(cucumbers, move_coords)

def part1(cucumbers: [str]) -> int:
    moved_east = True
    moved_south = True
    steps = 0
    while moved_east or moved_south:
        moved_east, cucumbers = step_east(cucumbers)
        moved_south, cucumbers = step_south(cucumbers)
        steps += 1
    return steps


def parse_input(filename) -> [(bool, int, int, int, int, int, int)]:
    file = open(filename)
    cucumbers = []
    for line in file.readlines():
        cucumbers.append([char for char in line.strip()])
    return cucumbers


if __name__ == '__main__':
    cucumbers = parse_input(F)
    print(f'part 1: {part1(cucumbers)}')  # 374
    print(f'part 2: {part2()}')  #
