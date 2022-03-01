import re


def meets_criteria(num):
    # REGEX'S ARE *GOOD*
    regex_arr = [
        '0{2}1*2*3*4*5*6*7*8*9*',
        '0*1{2}2*3*4*5*6*7*8*9*',
        '0*1*2{2}3*4*5*6*7*8*9*',
        '0*1*2*3{2}4*5*6*7*8*9*',
        '0*1*2*3*4{2}5*6*7*8*9*',
        '0*1*2*3*4*5{2}6*7*8*9*',
        '0*1*2*3*4*5*6{2}7*8*9*',
        '0*1*2*3*4*5*6*7{2}8*9*',
        '0*1*2*3*4*5*6*7*8{2}9*',
        '0*1*2*3*4*5*6*7*8*9{2}'
    ]

    # check that we have at least one occurence of double digits (not triple or more)
    # and that the digits are monotonically increasing
    for regex in regex_arr:
        if re.fullmatch(regex, str(num)):
            return True

    return False


def main():
    filename = 'input.txt'
    with open(filename, 'r') as file:
        input = file.read().split('-')
    begin = int(input[0])
    end = int(input[1])

    count = 0

    for i in range(begin, end+1):
        if meets_criteria(i):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
