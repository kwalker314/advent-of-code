import os

ROW_LENGTH = 7

if __name__ == '__main__':
    input_filename = "inputs\input" + os.path.basename(__file__)[-5:-3] + ".txt"
    #input_filename = "inputs/test.txt"

    part_1 = 0
    part_2 = 0
    seats = []
    for line in open(input_filename).readlines():
        line = line.strip()

        row = line[:ROW_LENGTH]
        row = int(row.translate(row.maketrans('FB', '01')), 2)

        col = line[ROW_LENGTH:]
        col = int(col.translate(col.maketrans('LR', '01')), 2)
        seat_num = row*8 + col

        part_1 = max(part_1, seat_num)
        seats += [seat_num]

    seats = sorted(seats)
    for i in range(1, len(seats)):
        if seats[i-1]+2 == seats[i]:
            part_2 = seats[i]-1

    print(f'part 1: {part_1}') #965
    print(f'part 2: {part_2}') #524