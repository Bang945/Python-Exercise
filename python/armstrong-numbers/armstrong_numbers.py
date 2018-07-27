def is_armstrong(number):
    def _power(d):
        return int(d) ** len(str(number))

    return sum(map(_power, str(number))) == number