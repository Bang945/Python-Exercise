from collections import Counter
import re


def word_count(phrase):
    phrase = re.sub("[^a-z0-9']+", ' ', phrase.lower())
    return Counter(map(lambda word: word.strip("'"),
                       ''.join(phrase).split()))