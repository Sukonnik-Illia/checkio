FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    representation = ''
    if number // 100:
        representation += FIRST_TEN[number//100-1] + ' ' + HUNDRED
        number -= (number//100)*100
    if (number // 10) > 1:
        if representation:
            representation += ' ' + OTHER_TENS[number//10 - 2]
        else:
            representation += OTHER_TENS[number//10 - 2]
        number -= (number//10)*10
    if (number // 10) == 1:
        if representation:
            representation += ' ' + SECOND_TEN[number % 10]
        else:
            representation += SECOND_TEN[number % 10]
        number == 0

    if (number//10) == 0 and (number % 10):
        if representation:
            representation += ' ' + FIRST_TEN[number - 1]
        else:
            representation += FIRST_TEN[number - 1]
    return representation

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '),\
        "Don't forget strip whitespaces at the end of string"
    print('done')
