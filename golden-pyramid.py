def rec(prev, pyra, l):
    if len(pyra) == 1:
        l.append(prev + pyra[0][0])
    else:
        pyra_a = [i[1:] for i in pyra[1:]]
        pyra_b = [i[:len(i)-1] for i in pyra[1:]]
        rec(prev+pyra[0][0], pyra_a, l)
        rec(prev+pyra[0][0], pyra_b, l)


def count_gold(pyra):
    """
    Return max possible sum in a path from top to bottom
    """
    l = []
    rec(0, pyra, l)
    return max(l)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
    print('done')
