import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import mstats

def calulateGammaAndEpsilon(bitarr):
    # get array of the mode of each column of bitarr
    mode = np.ma.masked_array.astype(
        np.ma.getdata(sp.stats.mstats.mode(bitarr))[0],
        dtype=np.int8)[0]

    # gamma: convert mode from binary to int
    g_binary = ''.join(map(str, mode.astype(int)))
    g = int(g_binary, 2)
    print("gamma:   ", g_binary, " / ", g)

    # epsilon: convert inverse of mode from binary to int
    e_binary = ''.join(map(str, np.logical_not(mode).astype(int)))
    e = int(e_binary, 2)
    print("epsilon: ", e_binary, " / ", e)

    # multiply to get our answer! (... for part 1 TT_TT)
    print("part 1: ", g * e)

def calculateO2andCO2(bitarr):
    #O2 first~
    o2__arr = bitarr.copy()
    i = 0
    while len(o2__arr)>1:
        o2__mode = np.ma.masked_array.astype(
            np.ma.getdata(sp.stats.mstats.mode(o2__arr))[0],
            dtype=np.int8)[0]

        o2__counts = np.ma.masked_array.astype(
            np.ma.getdata(sp.stats.mstats.mode(o2__arr))[1],
            dtype=np.int8)[0]

        mode_val = 1  # default behavior for if it's a 50/50 split
        if o2__counts[i] != len(o2__arr) / 2:
            mode_val = o2__mode[i]

        j = 0
        while j<len(o2__arr):
            # delete values that DO NOT match the mode at the index
            if o2__arr[j][i] != mode_val:
                o2__arr = np.delete(o2__arr, j, axis=0)
            else:
                # only increment j if we didn't delete something
                # (to prevent inadvertently skipping over something)
                j += 1

        i += 1

    #CO2 time!
    co2_arr = bitarr.copy()
    i = 0
    while len(co2_arr)>1:
        co2_mode = np.ma.masked_array.astype(
            np.ma.getdata(sp.stats.mstats.mode(co2_arr))[0],
            dtype=np.int8)[0]

        co2_counts = np.ma.masked_array.astype(
            np.ma.getdata(sp.stats.mstats.mode(co2_arr))[1],
            dtype=np.int8)[0]

        mode_val = 1  # default behavior for if it's a 50/50 split
        if co2_counts[i] != len(co2_arr) / 2:
            mode_val = co2_mode[i]

        j = 0
        while j<len(co2_arr) and len(co2_arr)>1:
            # delete values that DO match the mode at the index
            if co2_arr[j][i] == mode_val:
                co2_arr = np.delete(co2_arr, j, axis=0)
            else:
                # only increment j if we didn't delete something
                # (to prevent inadvertently skipping over something)
                j += 1

        i += 1

    # o2: convert from binary array to normal int
    o2_binary = ''.join(map(str, o2__arr[0].astype(int)))
    o2 = int(o2_binary, 2)
    print("o2:  ", o2_binary, " / ", o2)

    # co2: convert from binary array to normal int
    co2_binary = ''.join(map(str, co2_arr[0].astype(int)))
    co2 = int(co2_binary, 2)
    print("co2:  ", co2_binary, " / ", co2)

    print("part 2: ", o2*co2)


if __name__ == '__main__':
    input = "inputs/input03.txt"
    bitarr = np.genfromtxt(input, delimiter=1, dtype=np.int8)

    calulateGammaAndEpsilon(bitarr) #part 1
    calculateO2andCO2(bitarr) #part 2