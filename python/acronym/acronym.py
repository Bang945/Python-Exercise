def abbreviate(words):
    return ''.join(map(lambda word: word[:1].upper(), words.replace("-", " ").split()))
