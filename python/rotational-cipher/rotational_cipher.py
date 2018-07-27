import string


def rotate(text, key):
# Another sulotion
# From http://exercism.io/submissions/40089036e62f4b15b669a0e623d83957
#
#   tr = str.maketrans(ascii_lowercase+ascii_uppercase,
#       ascii_lowercase[key:]+ascii_lowercase[:key]+ascii_uppercase[key:]+ascii_uppercase[:key])
#   return text.translate(tr)

    def _encode(c):
        base = 'a' if c in string.ascii_lowercase else 'A'
        if c in string.ascii_letters:
            return chr((ord(c) + key) % ord(base) % 26 + ord(base))
        return c

    return ''.join(map(_encode, text))