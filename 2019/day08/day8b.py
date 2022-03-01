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
    arr = ['2' for i in range(width*height)]

    index = 0

    for chunk in chunks:
        index = 0
        for char in chunk:
            if (char == '0' or char == '1') and arr[index] == '2':
                arr[index] = char
            index += 1

    # ZYBLH - i just formatted in post (read: notepad++)
    print('\n'.join(wrap(''.join(arr), width)))


if __name__ == '__main__':
    main()
