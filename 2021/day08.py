import numpy as np
import re

if __name__ == '__main__':
    input = "inputs/input08.txt"
    letters = np.genfromtxt(input, delimiter='|', dtype=str, autostrip=True)
    letters_stripped = np.genfromtxt(input, delimiter=' ', dtype=str, autostrip=True, excludelist=['|'])

    decoded = ['']*10

    # 2-segment numbers: 1
    # 3-segment numbers: 7
    # 4-segment numbers: 4
    # 5-segment numbers: 2, 3, 5
    # 6-segment numbers: 0, 6, 9
    # 7-segment numbers: 8

    part_1 = 0
    for line in letters:
        arr = line[1].split(' ')
        i = 0
        for chars in arr:
            # part 1 - check for a 1, 7, 4, or 8, respectively
            if len(chars) == 2 or \
                    len(chars) == 3 or \
                    len(chars) == 4 or \
                    len(chars) == 7:
                part_1 += 1

    result = 0
    for line in letters:
        joined_line = ''.join(line[0])
        # store values in decoded for this line
        decoded[1] = ''.join(sorted(re.findall(r'\b[a-z]{2}\b', joined_line)[0])).strip()
        decoded[7] = ''.join(sorted(re.findall(r'\b[a-z]{3}\b', joined_line)[0])).strip()
        decoded[4] = ''.join(sorted(re.findall(r'\b[a-z]{4}\b', joined_line)[0])).strip()
        decoded[8] = ''.join(sorted(re.findall(r'\b[a-z]{7}\b', joined_line)[0])).strip()

        if decoded[1] == '' or decoded[7] == '' or decoded[4] == '' or decoded[8] == '':
            # sanity check that all lines have at least one 1, 4, 7, and 8
            print(f'missing ONES, FOURS, SEVENS, or EIGHTS for line: {line}')
            print(f'decoded: {decoded}')
            break

        fiveSegs = re.findall(r'\b[a-z]{5}\b', joined_line)
        for seg in fiveSegs:
            seg_sorted = ''.join(sorted(seg)).strip()
            matching = 0
            #2 shares exactly 2 segments with 4 (5 and 6 share 3)
            for char in decoded[4]:
                if seg.find(char) != -1:
                    matching += 1
            if matching == 2:
                decoded[2] = seg_sorted

            matching = 0
            #3 shares exactly 3 segments with 7 (2 and 5 share 2)
            for char in decoded[7]:
                if seg.find(char) != -1:
                    matching += 1
            if matching == 3:
                decoded[3] = seg_sorted

            if decoded[2] != '' and decoded[3] != '':
                break

        for seg in fiveSegs:
            seg_sorted = ''.join(sorted(seg)).strip()
            if seg_sorted != decoded[2] and seg_sorted != decoded[3]:
                decoded[5] = seg_sorted
                break

        if decoded[2] == '':
            print(f'missing TWOS for line: {line}')
            print(f'decoded: {decoded}')
            break
        if decoded[3] == '':
            print(f'missing THREES for line: {line}')
            print(f'decoded: {decoded}')
            break
        if decoded[5] == '':
            print(f'missing FIVES for line: {line}')
            print(f'decoded: {decoded}')
            break

        sixSegSeqs = re.findall(r'\b[a-z]{6}\b', joined_line)
        for seg in sixSegSeqs:
            seg_sorted = ''.join(sorted(seg)).strip()
            matching = 0
            #9 shares exactly 4 segments with 4 (0 and 6 share 3)
            for char in decoded[4]:
                if seg.find(char) != -1:
                    matching += 1
            if matching == 4:
                decoded[9] = seg_sorted

            matching = 0
            #6 shares exactly 2 segments with 7
            for char in decoded[7]:
                if seg.find(char) != -1:
                    matching += 1
            if matching == 2:
                decoded[6] = seg_sorted

            if decoded[6] != '' and decoded[9] != '':
                break

        for seg in sixSegSeqs:
            seg_sorted = ''.join(sorted(seg)).strip()
            if seg_sorted != decoded[9] and seg_sorted != decoded[6]:
                decoded[0] = seg_sorted
                break

        if decoded[0] == '':
            print(f'missing ZEROES for line: {line}')
            print(f'decoded: {decoded}')
            break
        if decoded[6] == '':
            print(f'missing SIXES for line: {line}')
            print(f'decoded: {decoded}')
            break
        if decoded[9] == '':
            print(f'missing NINES for line: {line}')
            print(f'decoded: {decoded}')
            break

        flattened_line = np.ndarray.flatten(line)
        line_result = 0
        for seg in line[1].split(' '):
            seg_sorted = ''.join(sorted(seg)).strip()
            line_result = line_result*10 + int(decoded.index(seg_sorted))
        result += int(line_result)
        decoded = [''] * 10

    print(f'part 1: {part_1}') #321 - what a nice answer!
    print(f'part 2: {result}') #1028926