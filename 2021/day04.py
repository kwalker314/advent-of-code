import numpy as np


def checkForWin(boards: np.ndarray) -> int:
    i = 0
    for board in boards:
        if -5 in np.sum(board, axis=0) or \
                -5 in np.sum(board, axis=1):
            return i
        else:
            i += 1
    return -1


def scoreBoard(board, move) -> int:
    return np.sum(board[board > 0]) * move


def deleteFinishedBoards(boards) -> np.ndarray:
    newBoards = np.copy(boards)
    i = 0
    # want to get down to just one so need to keep the number above 2
    while len(newBoards) > 2 and i < len(newBoards):
        if -5 in np.sum(boards[i], axis=0) or \
                -5 in np.sum(boards[i], axis=1):
            newBoards = np.delete(newBoards, i, axis=0)
        else:
            i += 1
    return newBoards


if __name__ == '__main__':
    input = open("inputs/input04.txt")

    moves = np.array(input.readline().split(',')).astype(int)

    boards = np.genfromtxt(input, dtype=np.int8, delimiter=3, skip_header=1, autostrip=True)
    boards = boards.reshape((100, 5, 5))  # group the boards properly
    #boards = boards.reshape((3, 5, 5))

    winningScore1 = 0
    winningScore2 = 0
    for move in moves:
        boards[boards == move] = -1  # mark the space(s) that contain the move number
        winningBoard = checkForWin(boards)

        if winningBoard > -1 and winningScore1 == 0:
                winningScore1 = scoreBoard(boards[winningBoard], move)

        while checkForWin(boards) > -1:
            winningScore2 = scoreBoard(boards[checkForWin(boards)], move)
            boards = np.delete(boards, checkForWin(boards), axis=0)

    print("part 1: ", winningScore1)
    print("part 2: ", winningScore2)
