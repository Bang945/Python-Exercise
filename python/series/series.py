def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError('ValueError') 

    return list(map(lambda i: series[i:i+length],  range(0, len(series) - length + 1)))