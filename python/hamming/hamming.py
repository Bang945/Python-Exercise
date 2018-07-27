from operator import ne

def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("a and b should be the same length")

    return sum(map(ne, strand_a, strand_b))