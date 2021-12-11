import numpy as np

if __name__ == '__main__':
    input = "inputs/input11.txt"
    score_1 = 0
    scores = []
    for chunk in open(input).readlines():
        stack = []
        finish_stack = True
        for char in chunk:
            if isOpeningChar(char):
                stack.append(char)
            elif isClosingChar(char) and charsMatch(char, stack[-1]):
                stack.pop()
            elif isClosingChar(char):
                score_1 += scoreChar(char)
                finish_stack = False
                break

        if finish_stack:
            chunk_score = 0
            for stack_char in reversed(stack):
                chunk_score = (5 * chunk_score) + scoreChar(stack_char)
            scores.append(chunk_score)
    scores.sort()
    print(f'part 1: {score_1}') #299793
    print(f'part 2: {scores[(len(scores)-1)//2]}')