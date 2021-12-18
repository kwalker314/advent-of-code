F = "inputs/input17.txt"
X_MIN, X_MAX, Y_MIN, Y_MAX = 0, 0, 0, 0
VX_MIN, VX_MAX, VY_MIN, VY_MAX = 0, 0, 0, 0

def initialize_constants():
    global X_MIN, X_MAX, Y_MIN, Y_MAX
    x, y = open(F).readline().strip().split(' ')[2:]
    x_range = x[:-1].split('=')[1].replace('..', ',').split(',')
    X_MIN, X_MAX = int(x_range[0]), int(x_range[1])

    y_range = y.split('=')[1].replace('..', ',').split(',')
    Y_MIN, Y_MAX = int(y_range[0]), int(y_range[1])

    global VX_MIN, VX_MAX, VY_MIN, VY_MAX

    vx_min_temp = 1
    while int(vx_min_temp * (vx_min_temp + 1) / 2) not in range(X_MIN, X_MAX + 1):
        vx_min_temp += 1
    VX_MIN = vx_min_temp

    VX_MAX = X_MAX
    VY_MIN = Y_MIN
    VY_MAX = -Y_MIN-1

    return X_MIN, X_MAX, Y_MIN, Y_MAX, VX_MIN, VX_MAX, VY_MIN, VY_MAX

def hits_target(x, y, vx, vy) -> (bool, int):
    if x > X_MAX or y < Y_MIN:
        return False, 0
    elif X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX:
        return True, y
    else:
        ret = hits_target(x+vx, y+vy, max(vx-1, 0), vy-1)
        return ret[0], max(y, ret[1])

if __name__ == '__main__':
    initialize_constants()
    highest_y = VY_MIN
    trajectories = 0
    for vy in reversed(range(VY_MIN, VY_MAX+1)):
        for vx in range(VX_MIN, VX_MAX+1):
            ret = hits_target(vx, vy, vx-1, vy-1)
            if ret[0]:
                if highest_y == VY_MIN:
                    highest_y = max(vy, ret[1])
                trajectories += 1

    print(f'part 1: {highest_y}') #5253
    print(f'part 2: {trajectories}') #1770