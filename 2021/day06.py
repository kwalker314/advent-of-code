import numpy as np

NEW_SPAWN_RATE = 8
SPAWN_RATE = 6
DAYS_1 = 80
DAYS_2 = 256

def processNumbers(fishNumbers):
    newFish = fishNumbers[0]
    i = 0
    newNumbers = fishNumbers.copy()
    while i < len(newNumbers)-1:
        newNumbers[i] = newNumbers[i+1]
        i += 1
    newNumbers[SPAWN_RATE] += newFish
    newNumbers[NEW_SPAWN_RATE] = newFish
    return newNumbers

if __name__ == '__main__':
    input = "inputs/input06.txt"
    fish = np.genfromtxt(input, delimiter=',', dtype=int)

    # for each i in fishNumbers[i], the value at the index is
    # how many fish have i more days until they spawn more fish
    fishNumbers = [0] * (NEW_SPAWN_RATE+1)
    for i in range(NEW_SPAWN_RATE):
        fishNumbers[i] = len(fish[fish == i])

    for i in range(DAYS_1):
        fishNumbers = processNumbers(fishNumbers)

    sum_1 = 0
    for num in fishNumbers:
        sum_1 += num

    print(f'sum: {sum_1}') #380612

    for i in range(DAYS_1, DAYS_2):
        fishNumbers = processNumbers(fishNumbers)

    sum_2 = 0
    for num in fishNumbers:
        sum_2 += num

    print(f'sum: {sum_2}')  # 1710166656900
