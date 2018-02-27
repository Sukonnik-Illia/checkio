NINETEEN = ["one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(n):
    r, n = ([NINETEEN[n // 100 - 1], HUNDRED] if n // 100 else []), n % 100
    r += [OTHER_TENS[n // 10 - 2]] + ([NINETEEN[n % 10 - 1]] if n % 10 else []) \
        if n // 20 else [NINETEEN[n-1]] if n else []

    return ' '.join(r)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), \
        "Don't forget strip whitespaces at the end of string"
    print('done')
