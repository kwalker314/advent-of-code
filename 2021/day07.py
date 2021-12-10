import numpy as np
if __name__ == '__main__':
    input = "inputs/input07.txt"
    crabs = np.genfromtxt(input, delimiter=',', dtype='int64')

    i = np.min(crabs) #start from the lowest number we can
    # ... but don't start with 0 for the first iteration or part 2's answer will get zeroed out
    if i < 1:
        i = 1

    max = np.max(crabs)
    min_1 = max * len(crabs) #reasonable maxess that are hopefully bigger than the actual answer!
    min_2 = min_1*min_1 #... this needed to be bigger than i initially estimated lol
    while i < max:
        abs_change = abs(crabs - i) #get the absolute change to get to i for each crab
        poss_min = np.sum(abs_change)
        if poss_min < min_1:
            min_1 = poss_min

        # sum of series! haven't done this in awhile - the formula for the sum of 1..n is:
        # f(n) = n(n+1)/2
        # so making our n be the same absolute difference from above...
        sum_change = np.array(abs_change*(abs_change + 1)/2).astype('int64') # ... and casting back to int...
        poss_min = np.sum(sum_change) # ... we get our adjusted possible minimum!
        if poss_min < min_2:
            min_2 = poss_min
        i += 1

    print(f'part 1: {min_1}') #342641
    print(f'part 2: {min_2}') #93006301