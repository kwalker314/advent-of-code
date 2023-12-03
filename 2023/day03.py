import os
import re
PART_NUM_PATTERN = re.compile(r'\d+')
SYMBOL_PATTERN = re.compile(r'[^\.^\d]')

class PartNum:
    def __init__(self, val, lineNum, start, end, xMax):
        self.val = val
        spaces = []
        # spaces above and below part number
        for x in range(max(start-1, 0), min(end+1, xMax)):
            spaces.append((lineNum-1)*xMax + x) if lineNum > 0 else None
            spaces.append((lineNum+1)*xMax + x)
        # spaces to the left and right of part number
        spaces.append(lineNum*xMax + start-1) if start > 0 else None
        spaces.append(lineNum*xMax + end) if end <= xMax else None
        self.spaces = spaces

input = open(os.path.join(os.getcwd(), "inputs/input03.txt"))
output1 = 0
output2 = 0
correctOutput = (528799, 84907174)
symbol_spaces = [] #each symbol's "index" within the grid
part_nums = [] #list of PartNum objects
gear_values = {} #each entry is {symbol_space: [adjacent_part_num1, adjacent_part_num2, ...]}
for lineNum, line in enumerate(input.readlines()):
    symbol_matches = re.finditer(SYMBOL_PATTERN, line.strip())
    #store match object as PartNum, which will auto-calculate the adjacent spaces for this part number
    for part_num_match in re.finditer(PART_NUM_PATTERN,line.strip()):
        part_nums.append(PartNum(int(part_num_match[0]), lineNum, part_num_match.start(), part_num_match.end(), len(line.strip())))
    #note down each symbol's "index" in the grid and add it to the gear dict if symbol is a "gear"
    for symbol_match in symbol_matches:
        space = len(line.strip())*lineNum+symbol_match.start()
        symbol_spaces.append(space)
        if (symbol_match[0] == '*'):
            gear_values.update({space: []})
input.close()

#add up all PartNums adjacent to a symbol and construct our gears dictionary
for part_num in part_nums:
    alreadyAdded = False
    for space in part_num.spaces:
        if not alreadyAdded and space in symbol_spaces:
            output1 += part_num.val
            alreadyAdded = True
        if space in gear_values:
            gear_values[space].append(part_num.val)

# add up the gear ratio (vals multiplied together) of all "gears" that have exactly two vals
output2 = sum(map(lambda vals: vals[0]*vals[1] if len(vals) == 2 else 0, gear_values.values()))
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)