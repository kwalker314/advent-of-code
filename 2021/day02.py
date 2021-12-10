if __name__ == '__main__':
    input = open("inputs/input02.txt")
    aim = 0
    forward = 0
    depth = 0

    for line in input.readlines():
        direction, amount = line.split()
        amount = int(amount)
        if direction == "forward":
            forward += amount
            depth += (aim*amount)
        if direction == "down":
            aim += amount
        if direction == "up":
            aim -= amount

    input.close()

    print("part 1: ", aim * forward)
    print("part 2: ", depth * forward)