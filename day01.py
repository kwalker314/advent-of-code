if __name__ == '__main__':
    input = open("inputs/input01.txt")
    totIncreases1 = 0
    totIncreases2 = 0
    first = int(input.readline())
    second = int(input.readline())
    third = int(input.readline())

    # initial calculations for part 1
    if second > first:
        totIncreases1 += 1
    if third > second:
        totIncreases1 += 1

    for nextVal in input.readlines():
        # check if simple increase from previous value
        if third < int(nextVal):
            totIncreases1 += 1

        # check if current 3-value window is increase from previous 3-value window
        if first < int(nextVal):
            totIncreases2 += 1

        #swap around values that we're keeping track of
        first, second, third = second, third, int(nextVal)
    input.close()

    print("part 1: ", totIncreases1)
    print("part 2: ", totIncreases2)