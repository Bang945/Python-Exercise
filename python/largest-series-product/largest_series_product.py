from functools import reduce


def largest_product(series, size):

    def _multiply(nums):
        return reduce(lambda x, y: int(x) * int(y), nums)

    if size < 0:
        raise ValueError("non negative size")
    if size == 0:
        return 1

    numbers = list(map(lambda i: series[i:i+size], range(0, len(series) - size + 1)))
    return max(map(_multiply, numbers))

    # return max(
    # reduce(mul, (int(n) for n in series[start : start + size]))
    # for start in range(0, len(series) - size + 1)
    #   )