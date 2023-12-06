import os
import re
import math
TIME_PATTERN = re.compile(r'^Time:\s+(.*)$')
DISTANCE_PATTERN = re.compile(r'^Distance:\s+(.*)$')

def quadraticFormula(a, b, c):
    x1 = (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)
    x2 = (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)
    min_x = math.ceil(min(x1, x2))
    max_x = math.floor(max(x1, x2))
    return max_x - min_x + 1

output1 = 1 #answers are multiplied together so start with 1 for outputs
output2 = 1
correctOutput = (800280, 45128024)
input = open(os.path.join(os.getcwd(), "inputs/input06.txt"))
raw_times = re.match(TIME_PATTERN, input.readline().strip())[1].split()
raw_distances = re.match(DISTANCE_PATTERN, input.readline().strip())[1].split()
times = [int(s) for s in raw_times]
distances = [int(s) for s in raw_distances]
input.close()
for total_seconds, distance_to_beat in zip(times, distances):
    # distance_to_beat+1 = ([seconds_pressed] m/s)*(total_seconds - seconds_pressed)
    # this is just the quadratic formula; ax^2 + bx + c = 0 form is as follows:
    # -seconds_pressed^2 + total_seconds*seconds_pressed - (distance_to_beat+1)
    # plugging these values into abc variables so it's easier to see the overall formula
    output1 *= quadraticFormula(-1, total_seconds, -distance_to_beat-1)

# part 2 - just join all values and push them through the quadratic formula function
# as one pair of total_time/distance_to_beat
overall_time = int(''.join(raw_times))
overall_distance = int(''.join(raw_distances))
output2 = quadraticFormula(-1, overall_time, -overall_distance-1)
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)