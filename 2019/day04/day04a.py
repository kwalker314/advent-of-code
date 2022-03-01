def meets_criteria(num):
    digits = [int(i) for i in str(num)]
    has_double = False
    for i in range(1, len(digits)):
        if digits[i-1] > digits[i]:
            return False
        if digits[i-1] == digits[i]:
            has_double = True

    return has_double


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
