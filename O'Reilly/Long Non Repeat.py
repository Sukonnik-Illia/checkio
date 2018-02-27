"""There are four substring missions that were born all in one day and you
shouldn’t be needed more than one day to solve them. All of those mission can
be simply solved by brute force, but is it always the best way to go? (you
might not have access to all of those missions yet, but they are going to be
available with more opened islands on the map).

A very similar to the first is the second mission of the series with only one
distinction is that you should look in a completely different way. You need to
find the first longest substring with all unique letters. For example, in
substring "abca" we have two substrings with unique letters "abc" and "bca",
but we should take the first one, so the answer is "abc".

Input: String.

Output: String.

"""
expected = [
    ('aaaaa', 'a'),
    ('abdjwawk', 'abdjw'),
    ('abcabcffab', 'abcf'),
    ('wq', 'wq'),
    ('fghfrtyfgh', 'ghfrty'),
]


def test(t_data):
    result = non_repeat(t_data[0])
    if result != t_data[1]:
        raise Exception('line = "{}"| expected = "{}"| result = "{}"'.format(
            t_data[0], t_data[1], result)
        )


def unique_substrings(line):
    index = start = 0
    for index, char in enumerate(line):
        substr = line[start: index]
        if len(substr) == len(set(substr)):
            yield substr
        else:
            start = start + 1

    substr = line[start: index+1]
    if len(substr) == len(set(substr)):
        yield substr


def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    return max(unique_substrings(line), key=len)


if __name__ == '__main__':
    for t_data in expected:
        test(t_data)
    print('Done!')
