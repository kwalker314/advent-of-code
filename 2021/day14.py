import numpy as np

STEPS_1 = 10
STEPS_2 = 40

def constructRules(polymers: np.ndarray):
    polymer_dict = {}
    for polymer in polymers:
        polymer1 = polymer[0][0]+polymer[1]
        polymer2 = polymer[1]+polymer[0][1]
        polymer_dict.update({polymer[0]: (polymer1, polymer2)})
    return polymer_dict

def freqDiff(pair_counts: dict, start: str, end: str) -> int:
    quants = {}
    for pair in pair_counts:
        count = pair_counts[pair]
        if pair[0] not in quants.keys():
            quants.update({pair[0]: count})
        else:
            quants[pair[0]] += count

        if pair[1] not in quants.keys():
            quants.update({pair[1]: count})
        else:
            quants[pair[1]] += count
    if start not in quants.keys():
        quants.update({start: 1})
    else:
        quants[start] += 1
    if end not in quants.keys():
        quants.update({end: 1})
    else:
        quants[end] += 1
    highest_freq = max(quants.values())
    lowest_freq = min(quants.values())
    return (highest_freq - lowest_freq)/2

if __name__ == '__main__':
    input = "inputs/input14.txt"
    #input = "inputs/test.txt"
    code = open(input).readline().strip()
    with open(input) as f:
        cleaned_polymers = (line.replace(' -> ', ',') for line in f)
        polymers = np.genfromtxt(cleaned_polymers, dtype=np.dtype('U'),
                                 autostrip=True, delimiter=',', skip_header=2)

    polymer_dict = constructRules(polymers)
    pair_counts = {}
    i = 1
    while i < len(code):
        pair = code[i-1]+code[i]
        if pair not in pair_counts.keys():
            pair_counts.update({pair: 1})
        else:
            pair_counts[pair] += 1
        i += 1

    part_1 = 0
    part_2 = 0
    for i in range(STEPS_2):
        temp = pair_counts.copy()
        for pair in temp:
            new_pairs = polymer_dict[pair]
            num_pairs = temp[pair]
            if new_pairs[0] not in pair_counts.keys():
                pair_counts.update({new_pairs[0]: num_pairs})
            else:
                pair_counts[new_pairs[0]] += num_pairs
            if new_pairs[1] not in pair_counts.keys():
                pair_counts.update({new_pairs[1]: num_pairs})
            else:
                pair_counts[new_pairs[1]] += num_pairs

            pair_counts[pair] -= num_pairs
        if i == STEPS_1-1:
            part_1 = freqDiff(pair_counts, code[0], code[-1])

    print(f'part 1: {int(part_1)}') #2797
    print(f'part 2: {int(freqDiff(pair_counts, code[0], code[-1]))}') #2926813379532