import unittest
import re as re
import ast

F = "inputs/input18.txt"

class Tests(unittest.TestCase):

    def test_getMagnitude(self):
        self.assertEqual(getMagnitude('[[1,2],[[3,4],5]]'), 143)
        self.assertEqual(getMagnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'), 1384)
        self.assertEqual(getMagnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]'), 445)
        self.assertEqual(getMagnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]'), 791)
        self.assertEqual(getMagnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]'), 1137)
        self.assertEqual(getMagnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'), 3488)

    def test_tryExplode(self):
        self.assertEqual(tryExplode('[[[[[9,8],1],2],3],4]'), '[[[[0,9],2],3],4]')
        self.assertEqual(tryExplode('[7,[6,[5,[4,[3,2]]]]]'), '[7,[6,[5,[7,0]]]]')
        self.assertEqual(tryExplode('[[6,[5,[4,[3,2]]]],1]'), '[[6,[5,[7,0]]],3]')
        self.assertEqual(tryExplode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),
                         '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
        self.assertEqual(tryExplode('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'),
                         '[[[[0,7],4],[15,[0,13]]],[1,1]]')
        self.assertEqual(tryExplode('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'),
                         '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(tryExplode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'),
                         '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
        self.assertEqual(tryExplode('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'),
                         '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]')

    def test_trySplit(self):
        self.assertEqual(trySplit('[[[[0,7],4],[15,[0,13]]],[1,1]]'),
                         '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
        self.assertEqual(trySplit('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'),
                         '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')
        self.assertEqual(trySplit('[10,5]'),
                         '[[5,5],5]')
        self.assertEqual(trySplit('[11,5]'),
                         '[[5,6],5]')
        self.assertEqual(trySplit('[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,10],20],[8,[9,0]]]]'),
                         '[[[[7,7],[7,8]],[[9,5],[8,0]]],[[[9,[5,5]],20],[8,[9,0]]]]')

    def test_reduce(self):
        self.assertEqual(reduce('[[[[1,1],[2,2]],[3,3]],[4,4]]'),
                         '[[[[1,1],[2,2]],[3,3]],[4,4]]')
        self.assertEqual(reduce('[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]'),
                         '[[[[3,0],[5,3]],[4,4]],[5,5]]')
        self.assertEqual(reduce('[[[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]],[6,6]]'),
                         '[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'),
                         '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(reduce('[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'),
                         '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
        self.assertEqual(reduce('[[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]'),
                         '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
        self.assertEqual(reduce('[[[[6,7],[0,[6,7]]],[[0,7],[7,21]]],[[2,[11,10]],[[0,8],[8,0]]]]'),
                         '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]')
        self.assertEqual(reduce('[[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'),
                         '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
        self.assertEqual(reduce('[[[[7,0],[7,8]],[[7,9],[0,6]]],[[[7,8],[0,6]],[[6,6],[[7,8],0]]]]'),
                         '[[[[7,0],[7,8]],[[7,9],[0,6]]],[[[7,8],[6,0]],[[6,6],[7,8]]]]')

    def test_puzzle(self):
        self.assertEqual(part1("inputs/test.txt"),
                         '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')

    def test_run_part1(self):
        self.assertEqual(getMagnitude(part1(F)), 3305)


def getMagnitude(nums_str: str) -> int:
    if nums_str.isdigit():
        return int(nums_str)
    else:
        nested_list = ast.literal_eval(nums_str)
        return (3 * getMagnitude(str(nested_list[0]))) + (2 * getMagnitude(str(nested_list[1])))


def trySplit(nums_str: str) -> str:
    last_find = 0
    found_nums = re.findall(r'[\d]+', nums_str)
    for i in range(len(found_nums)):
        num = found_nums[i]
        find = nums_str.find(num, last_find)
        last_find = nums_str.find(num, last_find)
        num = int(num)
        if num > 9:
            left = num // 2
            right = num - left
            literal = f'[{left},{right}]'
            nums_str = nums_str[:find] + literal + nums_str[find + len(str(num)):]
            return nums_str
        i += 1
    return nums_str


def tryExplode(nums_str: str) -> str:
    last_find = 0
    found_pairs = re.findall(r'\[[\d]+,[\d]+\]', nums_str)
    for search_pair in found_pairs:
        find = nums_str.find(search_pair, last_find)
        if find == -1:
            continue
        pair = search_pair[1:-1].split(',')
        num = pair[0]
        left = int(num)
        right = int(pair[1])
        literal = f'\[{left},{right}\]'
        if nums_str.count('[', 0, find) - nums_str.count(']', 0, find) >= 4:
            #find the digits to each side of the pair and store the character between the digit and pair
            prev_modify = re.compile(r'([\d]+)([^\d]+)' + literal).search(nums_str, last_find, find+len(search_pair))
            post_modify = re.compile(literal + r'([^\d]+)([\d]+)').search(nums_str, find)

            # if an addition happens to the left, the string to the left of the exploding pair is constructed as:
            # all the string to the left + addition result + left-side spacing
            # if an addition happens to the right, the string to the right of the exploding pair is reversed:
            # right-side spacing + addition result + rest of string to the right
            # regardless of where the numbers are exploding to, the pair is replaced with a zero
            if prev_modify and not post_modify:  # explode left only
                left_side = nums_str[:prev_modify.start()] + \
                            str(left + int(prev_modify.group(1))) + \
                            prev_modify.group(2)
                right_side = nums_str[find + len(search_pair):]
                return left_side + "0" + right_side
            elif prev_modify and post_modify:  # explode left _and_ right
                left_side = nums_str[:prev_modify.start()] + \
                            str(left + int(prev_modify.group(1))) + \
                            prev_modify.group(2)
                right_side = post_modify.group(1) + \
                             str(right + int(post_modify.group(2))) + \
                             nums_str[post_modify.end():]
                return left_side + "0" + right_side
            elif not prev_modify and post_modify:  # explode right only
                left_side = nums_str[:find]
                right_side = post_modify.group(1) + \
                             str(right + int(post_modify.group(2))) + \
                             nums_str[post_modify.end():]
                return left_side + "0" + right_side
        last_find = find + len(search_pair.split(',')[0])
    return nums_str


def reduce(line) -> str:
    line = line.strip().replace(' ', '')
    while True:
        reduced_line = tryExplode(line)
        if reduced_line == line:
            reduced_line = trySplit(line)
            if reduced_line == line:
                break
        line = reduced_line
    return line


def part1(filename: str):
    file = open(filename)
    prev_line = ''
    for line in file.readlines():
        if prev_line == '':
            prev_line = line.strip().replace(' ', '')
            continue
        line = line.strip().replace(' ', '')
        concat = f'[{prev_line},{line}]'
        prev_line = reduce(concat)
        print(prev_line)
        print('==============================')

    file.close()
    print(f'magnitude: {getMagnitude(prev_line)}')
    return prev_line


if __name__ == '__main__':
    print(f'part 1: {getMagnitude(part1(F))}')  # 3770 - too high; 4103 - too high
    print(f'part 2: {0}')  #
