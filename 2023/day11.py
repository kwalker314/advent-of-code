import os
import re
output1 = 0
output2 = 0
correctOutput = (9947476, 519939907614)
GALAXY_PATTERN = re.compile(r'#')

input = open(os.path.join(os.getcwd(), "inputs/input11.txt"))
galaxy_chart = []
galaxies = []
column_gaps = []
row_gaps = []
y = 0
for line in input:
    nextLine = line.strip()
    galaxy_chart.append(nextLine)
    if nextLine.find('#') < 0: #take note of rows that contain no galaxies
        row_gaps.append(y)
    else: #note galaxies
        galaxies.extend([(match.start(), y) for match in re.finditer(GALAXY_PATTERN, line)])
    y += 1
#take note of columns that contain no galaxies
for i in range(0, len(galaxy_chart[0])):
    if '#' not in [line[i] for line in galaxy_chart]:
        column_gaps.append(i)
#calculate distances
for index1, galaxy1 in enumerate(galaxies):
    if index1 == len(galaxies)-1:
        break
    for index2, galaxy2 in enumerate(galaxies[index1+1:]):
        x1 = min(galaxy1[0], galaxy2[0])
        x2 = max(galaxy1[0], galaxy2[0])
        xDelta = x2 - x1
        xGaps = len(list(filter(lambda column: x1 < column < x2, column_gaps)))
        
        y1 = min(galaxy1[1], galaxy2[1])
        y2 = max(galaxy1[1], galaxy2[1])
        yDelta = y2 - y1
        yGaps = len(list(filter(lambda column: y1 < column < y2, row_gaps)))

        #part 1 column/row gaps add one extra column/row
        #part 2 column/row gaps add 1000000-1=999999 extra columns/rows
        output1 += xDelta + xGaps + yDelta + yGaps
        output2 += xDelta + ((1000000-1)*xGaps) + yDelta + ((1000000-1)*yGaps)
input.close()
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)