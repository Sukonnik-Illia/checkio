from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1]) is True
    assert all_the_same([1, 2, 1]) is False
    assert all_the_same(['a', 'a', 'a']) is True
    assert all_the_same([]) is True
    assert all_the_same([1]) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
    print(
        "Coding complete? "
        "Click 'Check' to review your tests and earn cool rewards!"
    )
