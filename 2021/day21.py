DIE = 1

def update_die(new_value):
    global DIE
    DIE = new_value
    return DIE

def die_roll():
    die1 = 1 if DIE%101 == 0 else DIE%101
    die2 = 1 if (die1+1)%101 == 0 else (die1+1)%101
    die3 = 1 if (die2+1)%101 == 0 else (die2+1)%101
    update_die(1 if (die3+1)%101 == 0 else (die3+1)%101)
    return (die1+die2+die3)%10

if __name__ == '__main__':
    p1 = 1
    p2 = 6
    p1_score = 0
    p2_score = 0
    die = 1
    rolls = 0
    p1_turn = True
    while p1_score < 1000 and p2_score < 1000:
        roll = die_roll()
        rolls += 3
        #print(f'{"p1" if p1_turn else "p2"}\'s roll: {roll}')
        if p1_turn:
            p1 = 10 if (p1+roll)%10 == 0 else (p1+roll)%10
            p1_score += p1
        else: #p2's turn
            p2 = 10 if (p2+roll)%10 == 0 else (p2+roll)%10
            p2_score += p2
        print(f'{"p1" if p1_turn else "p2"}\'s new space: {p1 if p1_turn else p2}')
        p1_turn = not p1_turn
    print(f'total rolls: {rolls}')
    print(f'loser score: {min(p1_score, p2_score)}')
    print(rolls*min(p1_score, p2_score))