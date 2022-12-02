import os
import numpy as np

if __name__ == '__main__':
    input_filename = "inputs\input01.txt"
    nums = np.genfromtxt(input_filename, dtype=np.int64, delimiter=4, autostrip=True)
    winning_combo_1 = 0
    winning_combo_2 = 0
    while winning_combo_1 == 0 or winning_combo_2 == 0:
        num = nums[0]
        nums = nums[1:]
        for addNum in nums:
            if num+addNum == 2020 and winning_combo_1 == 0:
                winning_combo_1 = num * addNum
            for addNum2 in nums[1:]:
                if num+addNum+addNum2 == 2020 and winning_combo_2 == 0:
                    winning_combo_2 = num*addNum*addNum2
    print(f'part 1: {winning_combo_1}') #787776
    print(f'part 2: {winning_combo_2}') #262738554
