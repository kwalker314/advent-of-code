import numpy as np
import math

MISSING_PAREN_SCORE = 3
MISSING_BRACKET_SCORE = 57
MISSING_BRACE_SCORE = 1197
MISSING_ARROW_SCORE = 25137
ADD_PAREN_SCORE = 1
ADD_BRACKET_SCORE = 2
ADD_BRACE_SCORE = 3
ADD_ARROW_SCORE = 4

def isOpeningChar(char) -> bool:
    return char == '[' or char == '{' or char == '<' or char == '('

def isClosingChar(char) -> bool:
    return char == ']' or char == '}' or char == '>' or char == ')'

def charsMatch(char1, char2) -> bool:
    chars = {char1, char2}
    return chars == {'[', ']'} or chars == {'{', '}'} or \
        chars == {'(', ')'} or chars == {'<', '>'}

def scoreChar(char) -> int:
    if char == ')':
        return MISSING_PAREN_SCORE
    elif char == ']':
        return MISSING_BRACKET_SCORE
    elif char == '}':
        return MISSING_BRACE_SCORE
    elif char == '>':
        return MISSING_ARROW_SCORE
    elif char == '(':
        return ADD_PAREN_SCORE
    elif char == '[':
        return ADD_BRACKET_SCORE
    elif char == '{':
        return ADD_BRACE_SCORE
    elif char == '<':
        return ADD_ARROW_SCORE
    else:
        return 0

if __name__ == '__main__':
    input = "inputs/input10.txt"
    i = 0
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
    #2831395449 - too low
    #2929037097 - wrong