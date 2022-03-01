def parse_array(array):
    new_array = []
    currentX = 0
    currentY = 0
    new_array.append((currentX, currentY))

    for item in array:
        direction = item[0]
        if direction == 'U':
            currentY = currentY + int(item[1:])
        elif direction == 'D':
            currentY = currentY - int(item[1:])
        elif direction == 'L':
            currentX = currentX - int(item[1:])
        elif direction == 'R':
            currentX = currentX + int(item[1:])
        # add two instances of the coordinate bc we'll use the coordinate twice, ultimately
        # (once for the tail-end of the previous coordinate, and once for the front of the next one)
        new_array.extend([(currentX, currentY), (currentX, currentY)])

    # remove the final element - we don't need the first point for the next line
    # if the next line doesn't exist
    new_array.pop()

    return new_array.copy()


def sort_every_other_pair(array, vertical_start=1):
    i = 0
    vertical = []
    horizontal = []
    coord1 = (0, 0)
    coord2 = (0, 0)
    # sort by every other pair of coordinates
    if vertical_start:
        for item in array:
            coord1 = coord2
            coord2 = item
            if i < 2:
                vertical.append([coord1, coord2])
            else:
                horizontal.append([coord1, coord2])
            i += 1

            # reset the counter
            if i > 3:
                i = 0
    else:  # horizontal start
        for item in array:
            coord1 = coord2
            coord2 = item
            if i < 2:
                horizontal.append([coord1, coord2])
            else:
                vertical.append([coord1, coord2])
            i += 1

            # reset the counter
            if i > 3:
                i = 0

    return (vertical.copy(), horizontal.copy())


def is_intersection(v, h):
    # figure out the coordinates sitch
    (x11, y11) = v[0]
    (x12, y12) = v[1]
    (x21, y21) = h[0]
    (x22, y22) = h[1]

    # we will always assume v is vertical and h is horizontal

    # check if the y-coords of h (which are implicitly the same)
    # are in the range made by the y-coords of v
    if (((y11 < y21 < y12) or (y12 < y21 < y11)) and \
        # and that the x-coords of v (which are implicitly the same)
        # are in the range made by the x-coords of h
            ((x21 < x11 < x22) or (x22 < x11 < x21))):
            # return the manhattan distance of the intersection from the origin
        return abs(y21)+abs(x11)

    # check if the y-coords of v (which are implicitly the same)
    # are in the range made by the y-coords of h
    if (((y21 < y11 < y22) or (y22 < y11 < y21)) and \
        # and that the x-coords of h (which are implicitly the same)
        # are in the range made by the x-coords of v
            ((x11 < x21 < x12) or (x12 < x21 < x11))):
            # return the manhattan distance of the intersection from the origin
        return abs(y11)+abs(x21)

    # default return value - as big as we reasonably need
    return 10000


def main():
    input = ""
    filename = 'input.txt'
    with open(filename, 'r') as file:
        input = file.read()

    arrays = input.split('\n')
    wire1 = arrays[0].split(',')
    wire2 = arrays[1].split(',')

    # retain first char of both wires so we know orientation things
    firstchar1 = wire1[0][0]
    firstchar2 = wire2[0][0]

    # turn the arrays of directions into arrays of coordinates
    wire1 = parse_array(wire1)
    wire2 = parse_array(wire2)

    wire1v = []
    wire1h = []
    wire2v = []
    wire2h = []

    # split the arrays into their vertical and horizontal components
    if firstchar1 == "D" or firstchar1 == "U":
        (wire1v, wire1h) = sort_every_other_pair(wire1)
    else:
        (wire1v, wire1h) = sort_every_other_pair(wire1, 0)
    if firstchar2 == "D" or firstchar2 == "U":
        (wire2v, wire2h) = sort_every_other_pair(wire2)
    else:
        (wire2v, wire2h) = sort_every_other_pair(wire2, 0)

    # because surely no manhattan distance for this puzzle would be greater than... 2000?
    current_closest = 10000
    # ... this maximum estimate might be wrong. we'll see.

    # todo: write for loop to check all horizontal wire1 coords against all vertical wire2s,
    # and all vertical wire1 coords against all horizontal wire2s
    for line_v in wire1v:
        for line_h in wire2h:
            #print(f'line_v: {line_v}; line_h: {line_h}')
            distance = is_intersection(line_v, line_h)
            if distance < current_closest:
                current_closest = distance

    for line_v in wire2v:
        for line_h in wire1h:
            #print(f'line_v: {line_v}; line_h: {line_h}')
            distance = is_intersection(line_v, line_h)
            if distance < current_closest:
                current_closest = distance

    print(current_closest)


if __name__ == '__main__':
    main()
