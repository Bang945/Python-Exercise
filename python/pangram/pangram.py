def _is_letter(c):
	return (c >= 'a') and (c <= 'z')

def is_pangram(sentence):
    a_set = set(filter(_is_letter, sentence.lower()))
    return len(a_set) == 26