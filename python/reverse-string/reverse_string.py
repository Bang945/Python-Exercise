def reverse(input=''):
# solution 1:
    # return input[::-1]
# solution 2:
    if len(input) <= 1:
        return input
    return input[-1] + reverse(input[:-1])