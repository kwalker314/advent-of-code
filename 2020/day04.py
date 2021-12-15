import os
import re
REQ_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isValid(passport: str) -> bool:
    for field in REQ_FIELDS:
        if passport.find(field+":") == -1:
            return False
    return True

def isStrictValid(passport: str) -> bool:
    pass_len = len(passport)
    age_start = passport.find('byr:')+4
    age_end = passport.find(' ', age_start) if passport.find(' ', age_start) != -1 else pass_len
    if not (1920 <= int(passport[age_start:age_end]) <= 2002):
        return False

    iss_start = passport.find('iyr:') + 4
    iss_end = passport.find(' ', iss_start) if passport.find(' ', iss_start) != -1 else pass_len
    if not (2010 <= int(passport[iss_start:iss_end]) <= 2020):
        return False

    exp_start = passport.find('eyr:') + 4
    exp_end = passport.find(' ', exp_start) if passport.find(' ', exp_start) != -1 else pass_len
    if not (2020 <= int(passport[exp_start:exp_end]) <= 2030):
        return False

    height_start = passport.find('hgt:') + 4
    height_end = passport.find(' ', height_start) if passport.find(' ', height_start) != -1 else pass_len
    height = passport[height_start:height_end]
    # missing height units
    if height.isdigit():
        return False
    height_num = int(height[:-2])
    height_units = height[-2:]
    # invalid height number
    if (height_units not in ['cm', 'in']) or \
            (height_units == 'cm' and not (150 <= height_num <= 193)) or \
            (height_units == 'in' and not (59 <= height_num <= 76)):
        return False

    hcl_start = passport.find('hcl:') + 4
    hcl_end = passport.find(' ', hcl_start) if passport.find(' ', hcl_start) != -1 else pass_len
    hair_color = passport[hcl_start:hcl_end]
    if hair_color[0] != '#' or len(re.findall(r'[0-9a-f]{6}', hair_color[1:])) == 0:
        return False

    ecl_start = passport.find('ecl:') + 4
    ecl_end = passport.find(' ', ecl_start) if passport.find(' ', ecl_start) != -1 else pass_len
    eye_color = passport[ecl_start:ecl_end]
    if eye_color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid_start = passport.find('pid:') + 4
    pid_end = passport.find(' ', pid_start) if passport.find(' ', pid_start) != -1 else pass_len
    pid = passport[pid_start:pid_end]
    if not pid.isdigit() or len(pid) != 9:
        return False

    # default
    return True

if __name__ == '__main__':
    input_filename = "inputs\input" + os.path.basename(__file__)[-5:-3] + ".txt"
    #input_filename = "inputs/test.txt"
    prev_line = ''
    count_1 = 0
    count_2 = 0
    for line in open(input_filename).readlines():
        if prev_line == '':
            prev_line = line.replace('\n', '')
        elif line != '\n':
            prev_line = (prev_line + " " + line).replace('\n', '')
        elif prev_line != '':
            if isValid(prev_line):
                count_1 += 1
                if isStrictValid(prev_line):
                    count_2 += 1
            prev_line = line.replace('\n', '')
    #finish the last line that we have!
    if isValid(prev_line):
        count_1 += 1
        if isStrictValid(prev_line):
            count_2 += 1
    print(f'part 1: {count_1}') #192
    print(f'part 2: {count_2}') #101
