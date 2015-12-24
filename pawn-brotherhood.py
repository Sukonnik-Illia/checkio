def needed_prew_pawns(pawn):
    s = 'abcdefgh'
    prew_line = lambda: str(int(pawn[1])-1)
    if pawn[1] == '1':
        return tuple()
    elif pawn[0] == 'a' and pawn[0] != 'h':
        return ('b' + prew_line(),)
    elif pawn[0] == 'h':
        return ('g' + prew_line(),)
    else:
        return(s[s.index(pawn[0])-1]+prew_line(),
               s[s.index(pawn[0])+1]+prew_line())


def safe_pawns(pawns):
    n = 0
    for pawn in pawns:
        if any(map(lambda i: i in pawns, needed_prew_pawns(pawn))):
            n += 1
    return n

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
