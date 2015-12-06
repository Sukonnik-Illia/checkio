def checkio(game_result):

    rotate = lambda game_result: list(zip(*game_result[::-1]))

    check = ((game_result[i][i] for i in range(3)),
             (rotate(game_result)[i][i] for i in range(3)),
             *tuple(i for i in game_result),
             *(i for i in rotate(game_result)))
    if len(set(f_diagonal)) == 1 and '.' not in f_diagonal:
        return f_diagonal.pop()
    if len(set(s_diagonal)) == 1 and '.' not in s_diagonal:
        return s_diagonal.pop()

    for i in game_result:
        if len(set(i)) == 1:
            if set(i).pop() != '.':
                return set(i).pop()

    for i in rotate(game_result):
        if len(set(i)) == 1:
            if set(i).pop() != '.':
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
