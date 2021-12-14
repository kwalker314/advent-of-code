import numpy as np

def doFold(marks: np.ndarray, axis, i) -> np.ndarray:
    marks = np.delete(marks, i, axis) #delete the index to be used for the fold
    diff = marks.shape[axis] - (i * 2)

    split_marks = np.split(marks, [i], axis)

    if axis == 0:
        append_shape = (abs(diff), marks.shape[1])
    elif axis == 1:
        append_shape = (marks.shape[0], abs(diff))
    append = np.full(append_shape, False)

    if diff > 0: #split is before the halfway mark
        split_marks[0] = np.insert(split_marks[0], 0, append, axis)
    elif diff < 0: #split is after the halfway mark
        split_marks[1] = np.append(split_marks[1], append, axis)
    split_marks[1] = np.flip(split_marks[1], axis)
    folded_marks = np.logical_or(split_marks[0], split_marks[1])
    return folded_marks

if __name__ == '__main__':
    input = "inputs/input13.txt"
    coords = np.genfromtxt(input, dtype=np.int64, delimiter=',', skip_footer=11)
    instructions = np.genfromtxt(input, dtype=np.dtype('U20'), delimiter=' ', skip_header=921, usecols=2)

    max_x = np.max(coords, axis=0)[0]+1
    max_y = np.max(coords, axis=0)[1]+1
    marks = np.full((max_y, max_x), fill_value=False)
    for coordpair in coords:
        marks[coordpair[1]][coordpair[0]] = True

    marks_1 = 0
    for instruction in instructions:
        if instruction[0] == 'x':
            axis = 1
        elif instruction[0] == 'y':
            axis = 0
        i = int(instruction.split('=')[1])
        marks = doFold(marks, axis, i)
        if marks_1 == 0:
            marks_1 = len(marks[marks == True])

    print(f'part 1: {marks_1}') #775
    print(f'part 2:') #REUPUPKR
    for line in marks:
        line_str = ''
        for boolean in line:
            if boolean:
                line_str += '#'
            else:
                line_str += ' '
        print(line_str)

