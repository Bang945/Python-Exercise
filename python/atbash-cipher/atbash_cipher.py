import string

trans = dict(zip(string.ascii_lowercase + string.digits, string.ascii_lowercase[::-1] + string.digits))


def encode(plain_text):
    text = filter(lambda c: c in string.digits 
                            or c in string.ascii_lowercase, plain_text.lower())
    text = ''.join(map(lambda c:trans[c], text))
    return ' '.join(text[i:i+5] for i in range(0, len(text), 5))
    #translation = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
    #return stripped_text.translate(translation)


def decode(ciphered_text):
    return (encode(ciphered_text)).replace(" ", "")