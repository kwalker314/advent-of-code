import numpy as np

NEW_SPAWN_RATE = 9 #8+1 to account of timers being processed after spawn are added
SPAWN_RATE = 6
DAYS_1 = 80
DAYS_2 = 256

def spawnFish(fish: np.ndarray) -> np.ndarray:
    newFish = [NEW_SPAWN_RATE] * len(fish[fish == 0])
    currentFish = fish.copy()
    currentFish[currentFish < 0] = SPAWN_RATE
    return np.append(currentFish, newFish).astype(int)

def processTimers(fish: np.ndarray) -> np.ndarray:
    return fish - 1

if __name__ == '__main__':
    input = "inputs/input06.txt"
    fish = np.genfromtxt(input, delimiter=',', dtype=int)
    print(fish)

    for i in range(DAYS_1):
        fish = processTimers(spawnFish(fish))

    print(f'number of fish after {DAYS_1} days: {len(fish)}') #380612
