import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import mstats

if __name__ == '__main__':
    input = "inputs/input03.txt"
    bitarr = np.genfromtxt(input, delimiter=1, dtype=np.int8)

    mode = np.ma.masked_array.astype(
        np.ma.getdata(sp.stats.mstats.mode(bitarr))[0],
        dtype=np.int8)[0]

    gamma = int(''.join(map(str, mode.astype(int))), 2)
    print(gamma)
    epsilon = int(''.join(map(str, np.logical_not(mode).astype(int))), 2)
    print(epsilon)

    print("part 1: ", gamma*epsilon)
    print("part 2: ", "")