"""Here you should find the length of the longest substring that consists of
the same letter. For example, line "aaabbcaaaa" contains four substrings with
the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest
one which makes it an answer.

Input: String.

Output: Int.

"""


def isame(line):
    line = iter(line)
    try:
        prev = next(line)
    except StopIteration:
        yield 0
        raise StopIteration

    counter = 1
    for cur in line:
        if cur == prev:
            counter += 1
        else:
            yield counter
            counter = 1
            prev = cur
    yield counter


def long_repeat(line):
    return max(isame(line))


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
