import numpy as np

def isValidCave1(potentially_valid_cave: str, current_path: [str]) -> bool:
    return potentially_valid_cave.isupper() or potentially_valid_cave not in current_path

def isValidPath(path: [str]) -> bool:
    doubles = set()
    max_count = 0
    for item in path:
        if len(doubles) > 1 or max_count > 2:
            break
        if item.islower():
            count = path.count(item)
            max_count = max(max_count, count)
            if count > 1:
                doubles.add(item)
    return len(doubles) <= 1 and max_count <= 2

def neighbors1(caves, current_cave) -> {str}:
    neighbors = set()
    for cave in caves:
        if cave[0] == current_cave:
            neighbors.add(cave[1])
        elif cave[1] == current_cave:
            neighbors.add(cave[0])
    return neighbors

def neighbors2(caves, current_cave) -> {str}:
    neighbors = set()
    for cave in caves:
        cave0 = cave[0]
        cave1 = cave[1]
        if cave0 == current_cave and cave1 != 'start':
            neighbors.add(cave1)
        elif cave1 == current_cave and cave0 != 'start':
            neighbors.add(cave0)
    return neighbors

def exploreCaves1(caves: np.ndarray, current_cave: str, current_path: [str]) -> int:
    if current_cave == 'end':
        return 1
    paths_found = 0
    for neighbor in neighbors1(caves, current_cave):
        if isValidCave1(neighbor, current_path):
            paths_found += exploreCaves1(caves, neighbor, current_path + [current_cave])
    return paths_found

def exploreCaves2(caves: np.ndarray, current_path: [str]) -> int:
    last_cave = current_path[len(current_path)-1]
    if last_cave == 'end':
        #print(current_path)
        return 1
    paths_found = 0
    for neighbor in neighbors2(caves, last_cave):
        if neighbor.isupper() or isValidPath(current_path + [neighbor]):
            paths_found += exploreCaves2(caves, current_path + [neighbor])
    return paths_found

if __name__ == '__main__':
    input = "inputs/input12.txt"
    caves = np.genfromtxt(input, dtype=np.dtype('U5'), delimiter='-')
    num_paths_1 = 0
    num_paths_2 = 0
    for neighbor in neighbors1(caves, 'start'):
        num_paths_1 += exploreCaves1(caves, neighbor, ['start'])
    for neighbor in neighbors2(caves, 'start'):
        num_paths_2 += exploreCaves2(caves, ['start', neighbor])
    print(f'part 1: {num_paths_1}') #4775
    print(f'part 2: {num_paths_2}') #152480

