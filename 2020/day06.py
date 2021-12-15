import os

if __name__ == '__main__':
    input_filename = "inputs\input" + os.path.basename(__file__)[-5:-3] + ".txt"
    #input_filename = "inputs/test.txt"

    part_1 = 0
    part_2 = 0

    unique_answers = 0
    consensuses = 0
    curr_group = ''
    curr_group_len = 0
    for line in open(input_filename).readlines():
        line = line.strip()
        if line == '':
            if len(curr_group) > 0:
                unique_answers += len(set(curr_group))
                for char in set(curr_group):
                    if curr_group.count(char) == curr_group_len:
                        consensuses += 1
            curr_group = ''
            curr_group_len = 0
        else:
            curr_group += line
            curr_group_len += 1
    unique_answers += len(set(curr_group))
    for char in set(curr_group):
        if curr_group.count(char) == curr_group_len:
            consensuses += 1

    print(f'part 1: {unique_answers}') #6310
    print(f'part 2: {consensuses}') #3193