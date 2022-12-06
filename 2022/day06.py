import os

input = open(os.path.join(os.getcwd(), "inputs/input06.txt"))
line = input.readline().strip()
input.close()

WINDOW_SIZE1 = 4
WINDOW_SIZE2 = 14

part1 = 0
part2 = 0

for i in range(WINDOW_SIZE1,len(line)):
    # get the set of characters up to i for our current window size;
    # if the set size == the desired window size then save the value of i
    if part1 == 0 and len(set(line[i-WINDOW_SIZE1:i])) == WINDOW_SIZE1:
        part1 = i
    # if we haven't found the answer to part 1 yet
    # then part 2 is right out lol
    if part1 > 0 and len(set(line[max(0, i-WINDOW_SIZE2):i])) == WINDOW_SIZE2:
        part2 = i
    # once we find part 2 then that's curtains, baby!
    if part2 > 0:
        break

assert part1 == 1896, f'Part 1: expected 1896 but got {part1}'
assert part2 == 3452, f'Part 2: expected 3452 but got {part2}'

print("part 1: ", part1)
print("part 2: ", part2)