def create_intervals(data):
    """Create a list of intervals out of set of ints."""
    data = iter(sorted(data))
    prev = start = next(data)
    result = []
    for num in data:
        if num - 1 != prev:
            result.append((start, prev))
            start = num
        prev = num
    result.append((start, prev))
    return result


if __name__ == '__main__':
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == \
        [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Done!')
