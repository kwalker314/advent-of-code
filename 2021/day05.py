import math

import numpy as np
import re

def readInput() -> np.ndarray:
    input = open("inputs/input05.txt")
    coords = []

    for line in input.readlines():
        coords.extend(re.findall(r'\d+', line))
    coords = np.array(coords, dtype=np.int16).reshape((-1, 4))
    return coords

def isHorizOrVert(coords) -> bool:
    return coords[0] == coords[2] or coords[1] == coords[3]

def splitCoords(coords: np.ndarray) -> (np.ndarray, np.ndarray):
    i = 0
    straight_coords = coords.copy()
    for coord in coords:
        if isHorizOrVert(coord):
            i += 1
        else:
            straight_coords = np.delete(straight_coords, i, axis=0)
    i=0
    diag_coords = coords.copy()
    for coord in coords:
        if isHorizOrVert(coord):
            diag_coords = np.delete(diag_coords, i, axis=0)
        else:
            i += 1
    return (straight_coords, diag_coords)

def markHorizAndVerts(vents_map: np.ndarray, coords) -> np.ndarray:
    new_map = vents_map.copy()
    x = min(coords[0], coords[2])
    x_max = max(coords[0], coords[2])
    y_min = min(coords[1], coords[3])
    y_max = max(coords[1], coords[3])
    while x < x_max+1:
        y = y_min
        while y < y_max+1:
            new_map[x][y] += 1
            y += 1
        x += 1
    return new_map

def markDiagonals(vents_map: np.ndarray, coords) -> np.ndarray:
    new_map = vents_map.copy()

    x = coords[0]
    x2 = coords[2]
    x_diff = coords[2] - coords[0]
    x_inc = x_diff/abs(x_diff)

    y = coords[1]
    y_diff = coords[3] - coords[1]
    y_inc = y_diff/abs(y_diff)
    while x != x2:
        new_map[round(x)][round(y)] += 1 #round because bigger numbers become floats here by default or something
        x += x_inc
        y += y_inc

    #one final mark since we've reached the end of the line segment at this point!
    new_map[round(x)][round(y)] += 1
    return new_map

if __name__ == '__main__':
    allCoords = readInput()
    straightCoords,diagCoords = splitCoords(allCoords)

    maxes = np.max(allCoords, axis=0)

    x_max = max(maxes[0], maxes[2])+1
    y_max = max(maxes[1], maxes[3])+1

    vents_map_1 = np.zeros((x_max, y_max), dtype=np.int8)

    coordNum = 0
    #store marked map after only non-diagonal coordinates
    for coordPair in straightCoords:
        vents_map_1 = markHorizAndVerts(vents_map_1, coordPair)
        coordNum += 1

    vents_map_2 = vents_map_1.copy()
    #continue drawing on map with diagonal coordinates on top of straight coordinates

    for coordPair in diagCoords:
        vents_map_2 = markDiagonals(vents_map_2, coordPair)
        coordNum += 1

    print(f'part 1: {len(vents_map_1[vents_map_1 > 1])}') #6687
    print(f'part 2: {len(vents_map_2[vents_map_2 > 1])}') #19851