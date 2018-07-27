import string


def append(count):
    return (str(count) if count != 1 else "")


def decode(code):
    decoding = ''
    num = 0

    for index, value in enumerate(code):
        if value in string.digits:
            num = 10 * num + int(value)
        else:
            if num == 0:
                num = 1
            decoding += value*num
            num = 0

    return decoding


def encode(code):
    if not len(code):
        return ''

    encoding = ''
    count = 0
    base = code[0]

    for index, value in enumerate(code):
        if value == base:
            count += 1
        else:
            encoding += append(count) + base
            base = value
            count = 1
        if index == len(code) - 1:
            encoding += append(count) + value

    return encoding
