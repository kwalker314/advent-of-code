F = "inputs/input20.txt"
#F = "inputs/test.txt"


def add_padding(input_image: [str], padding: int, add_dot: bool) -> [str]:
    char = '.' if add_dot else '#'
    padding_lines = [[char] * (len(input_image[0]) + padding*2)] * padding
    edge_padding = [char] * padding
    for i in range(len(input_image)):
        input_image[i] = edge_padding + input_image[i] + edge_padding

    return padding_lines + input_image + padding_lines


def parse_input(filename: str) -> (str, [str]):
    file = open(filename)
    algorithm = file.readline().strip()
    input_image = []

    for line in file.readlines():
        if line == '\n':
            continue
        input_image.append([char for char in line.strip()])

    # print(f'algorithm: {algorithm}')
    # print(f'input image:')
    # for line in input_image:
    #     print(''.join(line))
    return algorithm, input_image


def decode(algorithm: str, input_image: [str]) -> [str]:
    output_image = []
    for i in range(1, len(input_image) - 1):
        output_line = []
        for j in range(1, len(input_image[i]) - 1):
            decoded = ''
            for i2 in range(i - 1, i + 2):
                for j2 in range(j - 1, j + 2):
                    decoded += '1' if input_image[i2][j2] == '#' else '0'
            decoded_num = int(decoded, 2)
            output_line.append(algorithm[decoded_num])
        output_image.append(output_line)
    return output_image


def part1(algorithm: str, input_image: [str]) -> int:
    output_image = decode(algorithm, add_padding(input_image, 2, True))
    output_image = decode(algorithm, add_padding(output_image, 2, False))
    for line in output_image:
        print(''.join(line))

    count = 0
    for line in output_image:
        count += ''.join(line).count('#')

    return count

def part2(algorithm: str, input_image: [str]) -> int:
    output_image = decode(algorithm, add_padding(input_image, 2, True))
    for i in range(1, 50):
        output_image = decode(algorithm, add_padding(output_image, 2, True if i % 2 == 0 else False))

    for line in output_image:
        print(''.join(line))

    count = 0
    for line in output_image:
        count += ''.join(line).count('#')

    return count


if __name__ == '__main__':
    algorithm, input_image = parse_input(F)
    print(f'part 1: {part1(algorithm, input_image)}')  # 5682
    print(f'part 2: {part2(algorithm, input_image)}')  # 17628