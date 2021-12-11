import numpy as np

STEPS = 100

def stepPropogate(octopi: np.ndarray, i, j, flashes: np.ndarray) -> (np.ndarray, np.ndarray):
    octo_copy = octopi.copy()
    flashes_copy = flashes.copy()
    if not flashes[i][j]:
        octo_copy[i][j] += 1
        if octo_copy[i][j] > 9:
            flashes_copy[i][j] = True
            octo_copy, flashes_copy = propogate(octo_copy, i, j, flashes_copy)
    return octo_copy, flashes_copy

def propogate(octopi, i, j, flashes) -> (np.ndarray, np.ndarray):
    octo_copy = octopi.copy()
    flashes_copy = flashes.copy()
    if i > 0 and j > 0:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i-1, j-1, flashes_copy) #up-left
    if i > 0:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i-1, j, flashes_copy)   #up
    if i > 0 and j < len(octo_copy[0])-1:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i-1, j+1, flashes_copy) #up-right
    if j > 0:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i, j-1, flashes_copy)   #left
    if j < len(octo_copy[0])-1:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i, j+1, flashes_copy)   #right
    if i < len(octo_copy)-1 and j > 0:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i+1, j-1, flashes_copy) #down-left
    if i < len(octo_copy)-1:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i+1, j, flashes_copy)   #down
    if i < len(octo_copy)-1 and j < len(octo_copy[0])-1:
        octo_copy, flashes_copy = stepPropogate(octo_copy, i+1, j+1, flashes_copy) #down-right
    return octo_copy, flashes_copy

if __name__ == '__main__':
    input = "inputs/input11.txt"
    flash_sum = 0
    octopi = np.genfromtxt(input, dtype=int, delimiter=1)
    flashes = np.full(octopi.shape, fill_value=False, dtype=bool)
    all_flash_step = ''
    step_num = 0
    while all_flash_step == '':
        octopi = octopi+1
        flashes[True] = False
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                if octopi[i][j] > 9 and not flashes[i][j]:
                    flashes[i][j] = True
                    octopi, flashes = propogate(octopi, i, j, flashes)
        octopi[octopi > 9] = 0
        flashes_to_add = len(flashes[flashes == True])
        step_num += 1
        if step_num <= STEPS:
            flash_sum += flashes_to_add
        if flashes_to_add == len(flashes.flatten()):
            all_flash_step = step_num
    print(f'part 1: {flash_sum}') #1562
    print(f'part 2: {all_flash_step}') #268

