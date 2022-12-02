import os

if __name__ == '__main__':
    input_filename = "inputs\input03.txt"
    slope_1 = 0
    slope_2 = 0
    slope_3 = 0
    slope_4 = 0
    slope_5 = 0
    i = 0
    j_1 = 0
    j_2 = 0
    j_3 = 0
    j_4 = 0
    for line in open(input_filename).readlines():
        line = line.strip()
        line_length = len(line)

        if line[j_1] == '#':
            slope_1 += 1
        if line[j_2] == '#':
            slope_2 += 1
        if line[j_3] == '#':
            slope_3 += 1
        if line[j_4] == '#':
            slope_4 += 1
        if i % 2 == 0 and line[int((i/2) % line_length)] == '#':
            slope_5 += 1

        j_1 = (j_1 + 1) % line_length
        j_2 = (j_2 + 3) % line_length
        j_3 = (j_3 + 5) % line_length
        j_4 = (j_4 + 7) % line_length
        i += 1
    print(f'part 1: {slope_2}') #237
    print(f'part 2: {slope_1*slope_2*slope_3*slope_4*slope_5}') #2106818610
