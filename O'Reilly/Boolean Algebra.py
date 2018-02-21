def checkio(a, b, op):
    methods = {
        'conjunction': '__and__',
        'disjunction': '__or__',
        'exclusive': '__rxor__',
        'equivalence': '__eq__',
        'implication': '__le__',
    }
    return getattr(a, methods[op])(b)

def boolean(a, b, op):
    methods = {
        'conjunction': '__and__',
        'disjunction': '__or__',
        'exclusive': '__rxor__',
        'equivalence': '__eq__',
        'implication': '__le__',
    }
    return getattr(a, methods[op])(b)


if __name__ == '__main__':
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('done')
