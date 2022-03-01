from textwrap import wrap
import re


def main():
    input = ""
    filename = 'input.txt'
    with open(filename, 'r') as file:
        input = file.read()

    width = 25
    height = 6

    chunks = wrap(input, width*height)

    smallest_zeros = width*height
    smallest_chunk = ''
    index = 0

    for chunk in chunks:
        current = len(re.findall('0', chunk))
        if current < smallest_zeros:
            smallest_zeros = current
            smallest_chunk = chunk
        index += 1  # increment index

    num_ones = len(re.findall('1', smallest_chunk))
    num_twos = len(re.findall('2', smallest_chunk))
    print(f'result: {num_ones*num_twos}')


if __name__ == '__main__':
    main()
