from collections import Counter

# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def straight(dice, ran):
    for i in ran:
        if i not in dice:
            return 0
    return 30


def score(dice, category):
    if category == CHOICE:
        return sum(dice)

    if category == LITTLE_STRAIGHT:
        return straight(dice, range(1, 6))

    if category == BIG_STRAIGHT:
        return straight(dice, range(2, 7))

    counter = Counter(dice)
    print(counter)
    if category in range(ONES, FULL_HOUSE):
        print(counter[category])
        return category * counter[category]

    if category == FOUR_OF_A_KIND:
        if max(counter.values()) >= 4:
            for k in counter:
                if counter[k] >= 4:
                    return k * 4
        else:
            return 0

    if category == YACHT:
        if 5 in counter.values():
            return 50
        return 0

    if category == FULL_HOUSE:
        if (max(counter.values()) >= 4 
                or 2 in Counter(counter.values()).values()):
            return 0
        return sum(dice)