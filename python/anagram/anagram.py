def detect_anagrams(word, candidates):
    return list(filter(lambda cand: 
                            sorted(cand.lower()) == sorted(word.lower())
                            and cand.lower() != word.lower(), 
                        candidates))