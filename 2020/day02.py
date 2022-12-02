import os
import numpy as np

if __name__ == '__main__':
    input_filename = "inputs\input02.txt"
    dt = [('lower_limit', np.int16), ('upper_limit', np.int16), ('letter', np.unicode_, 1), ('pw', np.dtype('U100'))]
    with open(input_filename) as f:
        cleanedlines = (line.replace('-', ' ').replace(':', '') for line in f)
        passwords = np.genfromtxt(cleanedlines, dtype=dt, autostrip=True, delimiter=' ')
    count_1 = 0
    count_2 = 0
    for password in passwords:
        letter = password['letter']
        pass_str = password['pw']
        lower_lim = password['lower_limit']
        upper_lim = password['upper_limit']
        pos1 = lower_lim - 1
        pos2 = upper_lim - 1

        if lower_lim <= pass_str.count(letter) <= upper_lim:
            count_1 += 1
        if (0 <= pos1 < len(pass_str) and pass_str[pos1] == letter) != (0 <= pos2 < len(pass_str) and pass_str[pos2] == letter):
            count_2 += 1
    print(f'part 1: {count_1}') #439
    print(f'part 2: {count_2}') #584
