from itertools import chain


def rotate(game_result):
    return list(zip(*game_result[::-1]))


def checkio(x):

    lines = (([x[i][i] for i in range(3)],
              [rotate(x)[i][i] for i in range(3)]),
             (i for i in x),
             (list(i) for i in rotate(x)))

    for i in chain.from_iterable(lines):
        if len(set(i)) == 1 and '.' not in i:
            return set(i).pop()

    return 'D'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print('done')
