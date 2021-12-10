import numpy as np

def isLowPoint(heatmap, i, j) -> int:
    current = heatmap[i][j]
    up = True
    down = True
    left = True
    right = True
    if i > 0:  # up
        up = heatmap[i - 1][j] > current
    if i < len(heatmap) - 1:  # down
        down = heatmap[i + 1][j] > current
    if j > 0:  # left
        left = heatmap[i][j - 1] > current
    if j < len(heatmap[0]) - 1:  # right
        right = heatmap[i][j + 1] > current
    if up and down and left and right:
        return current + 1
    else:
        return 0

def findBasin(heatmap: np.ndarray, i, j) -> (int, np.ndarray):
    new_heatmap = heatmap.copy()
    current = new_heatmap[i][j]
    new_heatmap[i][j] = 9
    basin_size = 1
    if i > 0 and new_heatmap[i-1][j] != 9: #up
        ret = findBasin(new_heatmap, i-1, j)
        basin_size += ret[0]
        new_heatmap = ret[1]
    if i < len(new_heatmap)-1 and new_heatmap[i+1][j] != 9: #down
        ret = findBasin(new_heatmap, i+1, j)
        basin_size += ret[0]
        new_heatmap = ret[1]
    if j > 0 and new_heatmap[i][j-1] != 9: #left
        ret = findBasin(new_heatmap, i, j-1)
        basin_size += ret[0]
        new_heatmap = ret[1]
    if j < len(new_heatmap[0])-1 and new_heatmap[i][j+1] != 9: #right
        ret = findBasin(new_heatmap, i, j+1)
        basin_size += ret[0]
        new_heatmap = ret[1]
    return basin_size, new_heatmap

if __name__ == '__main__':
    input = "inputs/input09.txt"
    heatmap = np.genfromtxt(input, delimiter=1, dtype=int)
    basins = heatmap.copy()
    sum = 0
    i = 0
    basin_size_1 = 1
    basin_size_2 = 1
    basin_size_3 = 1
    for i in range(len(heatmap)):
        j = 0
        for j in range(len(heatmap[0])):
            lowPoint = isLowPoint(heatmap, i, j)
            sum += lowPoint

            if lowPoint > 0:
                (basin_size, basins) = findBasin(basins, i, j)
                if basin_size > basin_size_1:
                    basin_size_1, basin_size_2, basin_size_3 = basin_size, basin_size_1, basin_size_2
                elif basin_size > basin_size_2:
                    basin_size_2, basin_size_3 = basin_size, basin_size_2
                elif basin_size > basin_size_3:
                    basin_size_3 = basin_size

    print(f'sum: {sum}') #496
    print(f'basin_size: {basin_size_1*basin_size_2*basin_size_3}') #902880