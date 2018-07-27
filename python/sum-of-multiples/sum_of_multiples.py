def sum_of_multiples(limit, multiples):
    nums = set()
    for multi in multiples:
        nums.update(set(range(0, limit, multi)))
    return sum(nums)