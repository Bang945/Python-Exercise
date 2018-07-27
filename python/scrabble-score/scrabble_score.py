from collections import Counter


SCRABLE_SET_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T')
SCRABLE_SET_2 = ('D', 'G')
SCRABLE_SET_3 = ('B', 'C', 'M', 'P')
SCRABLE_SET_4 = ('F', 'H', 'V', 'W', 'Y')
SCRABLE_SET_5 = ('K')
SCRABLE_SET_8 = ('J', 'X')
SCRABLE_SET_10 = ('Q', 'Z')

SCRABLE_TABLE = (SCRABLE_SET_1, SCRABLE_SET_2, 
                 SCRABLE_SET_3, SCRABLE_SET_4, 
                 SCRABLE_SET_5, SCRABLE_SET_8,
                 SCRABLE_SET_10)

SCORES = [1, 2, 3, 4, 5, 8, 10]

def score(word):
    counter = Counter(word.upper())
    print(counter)

    sum = 0
    for w in counter:
        for i in range(0, 7):
            if w in SCRABLE_TABLE[i]:
                sum += SCORES[i] * counter[w]
    return sum
