DIE = 1
WINS = (0, 0)
POSS_POSITIONS = 10
POSS_NON_WIN_SCORES = 21
# for each x, y in POSS_ROLLS, x is the sum of the 3 rolls,
# and y is the frequency of that sum out of every combination of rolls
POSS_ROLLS = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def update_die(new_value):
    global DIE
    DIE = new_value
    return DIE


def die_roll():
    die1 = 1 if DIE % 101 == 0 else DIE % 101
    die2 = 1 if (die1 + 1) % 101 == 0 else (die1 + 1) % 101
    die3 = 1 if (die2 + 1) % 101 == 0 else (die2 + 1) % 101
    update_die(1 if (die3 + 1) % 101 == 0 else (die3 + 1) % 101)
    return (die1 + die2 + die3) % 10


def part1(p1: int, p2: int):
    update_die(1)
    p1_score = 0
    p2_score = 0
    rolls = 0
    p1_turn = True
    while p1_score < 1000 and p2_score < 1000:
        roll = die_roll()
        rolls += 3
        if p1_turn:
            p1 = 10 if (p1 + roll) % 10 == 0 else (p1 + roll) % 10
            p1_score += p1
        else:  # p2's turn
            p2 = 10 if (p2 + roll) % 10 == 0 else (p2 + roll) % 10
            p2_score += p2
        p1_turn = not p1_turn
    return rolls * min(p1_score, p2_score)


def update_wins(num_wins: int, p1_turn: bool):
    global WINS
    if p1_turn:
        WINS = (WINS[0] + num_wins, WINS[1])
    else:
        WINS = (WINS[0], WINS[1] + num_wins)
    return WINS


def initialize_scores_array() -> [int]:
    return [[[[0 for _ in range(POSS_POSITIONS)] for _ in range(POSS_NON_WIN_SCORES)] for _ in range(POSS_POSITIONS)] for _ in range(POSS_NON_WIN_SCORES)]


def progress_scores(p1_turn: bool, scores: [int]) -> (bool, [int]):
    continue_play = False

    # for the sake of readability in this function,
    # p1 is always the current player, and p2 is always the other player
    scores_copy = initialize_scores_array()

    for p1_score in range(POSS_NON_WIN_SCORES-1):
        for p1_pos in range(POSS_POSITIONS):
            # adjust the position of player 1 to account for a board that goes from 1-10, rather than 0-9
            p1_pos_adj = p1_pos + 1
            for p2_score in range(POSS_NON_WIN_SCORES):
                for p2_pos in range(POSS_POSITIONS):
                    num = scores[p1_score][p1_pos][p2_score][p2_pos]
                    if num == 0:
                        continue
                    elif p1_score == 20:
                        # multiply by 3 because this score would have won in all
                        # 3 universes created by rolling the dice
                        update_wins(num*3, p1_turn)
                    else:
                        for roll, multiply in POSS_ROLLS:
                            new_pos = 10 if (p1_pos_adj + roll) % 10 == 0 else (p1_pos_adj + roll) % 10
                            new_score = p1_score + new_pos
                            if new_score >= 21:
                                update_wins(num*multiply, p1_turn)
                            else:
                                continue_play = True
                                # don't forget to adjust the position back down again
                                scores_copy[p2_score][p2_pos][new_score][new_pos - 1] += num*multiply

    return continue_play, scores_copy


def part2(p1: int, p2: int):
    p1_turn = True
    continue_play = True

    # scores array is always from the most recent player's perspective;
    # for a given state scores[a][b][c][d] = x,
    # - a is the current player's score, up to 20 (the maximum possible score without a win)
    # - b the board placement, so b is a range 0-9 for board positions 1-10, respectively
    # - c and d is like scores[a] and scores[a][b], but for the other player
    # - ... and x is the number of universes where a, b, c, and d are the case
    # so! to summarize, scores[a][b][c][d] stores the number of universes where:
    # - the current player has a score a at board position b (plus 1)
    # - and the other player has a score c on board position d (plus 1)
    #
    # functionally, evey time a turn happens, we do the following:
    # 1. make a copy of scores with all values set to 0 (score_copy)
    # 2. for each score[a][b][c][d] in score[a], for each roll, multiply tuple in POSS_ROLLS,
    #    calculate the new position on the board (new_pos) and the resulting new score (new_score)
    #    a. if new_score >= 21, add value in score[a][b][c][d] to current player's win count and continue
    #       i. this effectively removes the set of universes from play, as the other player should not
    #          continue to make moves, as they have lost at that point
    #    b. otherwise, add the value of score[a][b][c][d] to score_copy[c][d][a+new_score][new_pos-1] and
    #       make set a boolean (continue_play) to True to know that the process must repeat
    #       i. NOTE that [a][b] and [c][d] get swapped here to play from the other player's perspective!
    # 3. if continue_play is True, set p1_turn = not p1_turn and scores = scores_copy,
    #    then go back to step 1 to repeat the process
    scores = initialize_scores_array()  # a 21 x 10 x 21 x 10 array
    scores[0][p1][0][p2] = 1  # initialize using the starting values
    while continue_play:
        continue_play, scores = progress_scores(p1_turn, scores)
        p1_turn = not p1_turn
        print(f'P1 WINS: {WINS[0]} // P2 WINS: {WINS[1]}')

    return max(WINS[0], WINS[1])


if __name__ == '__main__':
    #p1, p2 = 1, 6
    p1, p2 = 4, 8 #test input
    print(f'part 1: {part1(p1, p2)}')
    print(f'part 2: {part2(p1, p2)}') #225525006757890 - too high;
    # 2297753325
    # 2425313016 - too low
