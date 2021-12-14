import numpy as np

STEPS_1 = 10
STEPS_2 = 40

def polymerize(polymers: np.ndarray, codePair: str) -> str:
    for polymer in polymers:
        if polymer[0] == codePair:
            return codePair[0]+polymer[1]+codePair[1]
    return ''

def processPolymer(polymers: np.ndarray, code: str) -> str:
    i = 1
    while i < len(code):
        pair = code[i-1]+code[i]
        polymerization = polymerize(polymers, pair)
        if polymerization != '':
            pre_code = code[:i-1]
            post_code = code[i+1:] if i+1 < len(code) else ''
            code = pre_code+polymerization+post_code
            i += 1
        i += 1
    return code

if __name__ == '__main__':
    input = "inputs/input14.txt"
    code = open(input).readline().strip()
    with open(input) as f:
        cleaned_polymers = (line.replace(' -> ', ',') for line in f)
        polymers = np.genfromtxt(cleaned_polymers, dtype=np.dtype('U'),
                                 autostrip=True, delimiter=',', skip_header=2)

    for i in range(STEPS_1):
        code = processPolymer(polymers, code)

    highest_freq_1 = 0
    lowest_freq_1 = len(code)
    for unique_letter in set(code):
        count = code.count(unique_letter)
        if count > highest_freq_1:
            highest_freq_1 = count
        if count < lowest_freq_1:
            lowest_freq_1 = count

    print(f'part 1: {highest_freq_1 - lowest_freq_1}') #2797
    print(f'part 2: {0}') #