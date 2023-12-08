import os
import re
import operator as op
INPUT_PATTERN = re.compile(r'^([A-Za-z0-9]+)\s+(\d+)$')

output1 = 0
output2 = 0
correctOutput = (248113761, 246285222)

PART1_HAND_LETTERS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9":  9,
    "8":  8,
    "7":  7,
    "6":  6,
    "5":  5,
    "4":  4,
    "3":  3,
    "2":  2,
}
    
class CamelHand:
    useJokers = False
    def __init__(self, hand, bid):
        self.handLetters = hand
        self.hand = []
        for handLetter in list(hand):
            self.hand.append(PART1_HAND_LETTERS[handLetter])
        self.type = self._get_type()
        self.type_jokerfied = self._get_joker_type()
        self.bid = int(bid)
    '''joker type outcomes (assuming a hand is 5 cards):
    |===============|========|================|
    | base type     | jokers |  best outcome  |
    |---------------|--------|----------------|
    | 0 (high hand) |   1    | 1pair => 1     |
    | 1 (1 pair)    |   1    | 3oak => 3      |
    | 1 (1 pair)    |   2    | 3oak => 3      |
    | 2 (2 pair)    |   1    | 3oak+pair => 4 |
    | 2 (2 pair)    |   2    | 4oak => 5      |
    | 3 (3oak)      |   1    | 4oak => 5      |
    | 3 (3oak)      |   3    | 4oak => 5      |
    | 4 (3oak+pair) |   2    | 5oak => 6      |
    | 4 (3oak+pair) |   3    | 5oak => 6      |
    | 5 (4oak)      |   1    | 5oak => 6      |
    | 5 (4oak)      |   4    | 5oak => 6      |
    | 6 (5oak)      |   5    | 5oak => 6      |
    |===============|========|================|
    '''
    def _get_joker_type(self):
        jokerCount = op.countOf(self.hand, PART1_HAND_LETTERS['J'])
        if self.type == 6 or jokerCount == 0:
            return self.type
        # any number of jokers increases the type value in most cases!
        if self.type == 5 or self.type == 4:
            return 6
        if self.type == 3:
            return 5
        if self.type == 2:
            if jokerCount == 2:
                return 5
            else: # jokerCount == 1
                return 4
        if self.type == 1:
            return 3
        else:
            return 1

    def _get_type(self, useJokerHand=False):
        ''' 6 = Five of a kind,
            5 = four of a kind,
            4 = full house (3 of one kind, 2 of another),
            3 = three of a kind
            2 = two pairs,
            1 = one pair,
            0 = high hand (all unique cards)
        '''
        cardCounts = {}
        cards = self.hand_jokerfied if useJokerHand else self.hand
        for card in cards:
            if card in cardCounts.keys():
                cardCounts[card] += 1
            else:
                cardCounts[card] = 1
        foundPairs = 0
        foundTriplets = 0
        for val in cardCounts.values():
            if val == 5:
                return 6
            elif val == 4:
                return 5
            elif val == 3:
                foundTriplets = 1
            elif val == 2:
                foundPairs += 1
        if foundTriplets > 0:
            if foundPairs > 0:
                return 4
            else:
                return 3
        if foundPairs > 1:
            return 2
        elif foundPairs > 0:
            return 1
        return 0
    def _compHands(self, other):
        for s, o in zip(self.hand, other.hand):
            s = 1 if self.useJokers and s == PART1_HAND_LETTERS['J'] else s
            o = 1 if other.useJokers and o == PART1_HAND_LETTERS['J'] else o
            if s > o:
                return 1
            elif s < o:
                return -1
        return 0
    def __lt__(self, other):
        selfType = self.type_jokerfied if self.useJokers and other.useJokers else self.type
        otherType = other.type_jokerfied if self.useJokers and other.useJokers else other.type
        if selfType < otherType:
            return True
        if selfType > otherType:
            return False
        return self._compHands(other) == -1
    def __eq__(self, other):
        selfType = self.type_jokerfied if self.useJokers and other.useJokers else self.type
        otherType = other.type_jokerfied if self.useJokers and other.useJokers else other.type
        return selfType == otherType and self._compHands(other) == 0
    def __repr__(self):
        return f'\nCamelHand(type: {self.type}, bid: {self.bid},hand: {self.hand})'
input = open(os.path.join(os.getcwd(), "inputs/input07.txt"))
hands = []
for line in input:
    (hand, bid) = re.match(INPUT_PATTERN, line.strip()).group(1, 2)
    hands.append(CamelHand(hand, bid))
input.close()
index = 1
# part 1 calcs
for hand in sorted(hands):
    score = index*hand.bid
    output1 += (index*hand.bid)
    index += 1
    hand.useJokers = True #setting up for part 2 tho
# part 2 calcs
index = 1
for hand in sorted(hands):
    score = index*hand.bid
    output2 += (index*hand.bid)
    index += 1
assert output1 == correctOutput[0], f'Part 1: expected {correctOutput[0]} but got {output1}'
assert output2 == correctOutput[1], f'Part 2: expected {correctOutput[1]} but got {output2}'
print("part 1: ", output1)
print("part 2: ", output2)