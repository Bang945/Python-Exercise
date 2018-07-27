import string


def to_int(s):
    return 10 if s == 'X' else int(s)


def verify(isbn):
    isbn = isbn.replace('-', '')
    if (len(isbn) != 10
            or not isbn[:-1].isdigit()
            or isbn[-1] not in (string.digits + 'X')):
        return False

    numbers = ((10 - i) * to_int(v) for i, v in enumerate(isbn))
    return sum(numbers) % 11 == 0