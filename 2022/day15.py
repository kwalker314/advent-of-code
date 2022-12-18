import os
import re
from collections import namedtuple
BeaconSensor = namedtuple('BeaconSensor', ['beacon', 'sensor'])
Point = namedtuple('Point', ['x', 'y'])
input = open(os.path.join(os.getcwd(), "inputs/input15.txt"))

def getMaxManhattanDist(bs: BeaconSensor) -> int:
    return abs(bs.beacon.x - bs.sensor.x) + abs(bs.beacon.y - bs.sensor.y)

def getHorizontalLimits(y: int, bs: BeaconSensor) -> [int]:
    maxDist = getMaxManhattanDist(bs)
    # get the horizontal "leeway" we have outside of the distance
    # we need to simply get from the sensor's y-coordinate
    # to the required y-coordinate
    xPlusMinus = maxDist - abs(bs.sensor.y - y)
    print('\n========== ', bs, ' ==========')
    # print(maxDist)
    if xPlusMinus < 0:
        return []
    # print('xPlusMinus', xPlusMinus)
    xLimits = [bs.sensor.x - xPlusMinus, bs.sensor.x + xPlusMinus]
    # print(xLimits)
    return [Point(x, y) for x in range(xLimits[0], xLimits[1]+1)]

def constructBeaconSensor(line: str) -> BeaconSensor:
    coords = list(map(int, re.findall(r'-?\d+', line)))
    return BeaconSensor(Point(coords[2], coords[3]), Point(coords[0], coords[1]))

beaconsAndSensors = []
for line in input.readlines():
    beaconsAndSensors.append(constructBeaconSensor(line.strip()))
input.close()

takenPoints = set()
for bs in beaconsAndSensors:
    takenPoints.update(getHorizontalLimits(2000000, bs))

# exclude beacons from the final count of spaces where a beacon cannot be
part1, part2 = len(takenPoints.difference([bs.beacon for bs in beaconsAndSensors])), 0
# assert part1 == 25248, f'Part 1: expected 25248 {part1}'
# assert part2 == 25248, f'Part 2: expected 25248 {part2}'
print("part 1: ", part1)
print("part 2: ", part2)