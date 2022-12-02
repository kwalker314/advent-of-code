import os
import sys

# points we get if we win with a given hand
self_score = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3, # scissors
}
# for the self_[outcome] dictionaries, the key
# is the opponent's hand and the value is our hand,
# so self_win["A"] holds the hand we would need to
# play to win if the opponent has a hand of "A"
self_win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
self_draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
self_lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
# map the desired outcome to the dictionary
# we use for that outcome, kinda like a derivative
# of part 1
# ... or an integral, i guess?
outcome = {
    "X": self_lose,
    "Y": self_draw,
    "Z": self_win,
}

def calculateScore1(opponent, you):
    score = self_score[you]

    if self_win[opponent] == you:
        score += 6
    elif self_draw[opponent] == you:
        score += 3
    # a loss awards 0 points

    return score

def calculateScore2(opponent, you):
    # added layer of complexity - now the "you" value is the outcome we want
    # (win, loss, draw), so use the outcome dictionary to map the desired
    # outcome to the correct map to score it based on the opponent's move
    return calculateScore1(opponent, outcome[you][opponent])

input = open(os.path.join(os.getcwd(), "inputs/input02.txt"))
final_score1 = 0
final_score2 = 0
for line in input:
    opponent, you = line.strip().split(' ')
    final_score1 += calculateScore1(opponent, you)
    final_score2 += calculateScore2(opponent, you)
input.close()
print("part 1: ", final_score1)
print("part 2: ", final_score2)
