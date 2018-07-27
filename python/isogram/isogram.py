import string

def is_letter(c):
	return c.lower() in set(string.ascii_lowercase)
    
def is_isogram(string):
    string = list(filter(is_letter, string.lower()))
    return len(string) == len(set(string))