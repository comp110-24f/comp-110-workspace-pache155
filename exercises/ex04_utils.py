"""m"""

__author__ = "730741697"


def all(a: list[int], b: int) -> bool:
    """Indicates if whether or not a list is made up of one given integer"""
    i = 0
    c = 0
    while i < len(a):
        if a[i] == b:
            c += 1
            i += 1
        else:
            i += 1
    if c == len(a):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Returns the largest value in a list"""
    i = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while len(input) > 1:
            if input[i] < input[i + 1]:
                input.pop(i)
            elif input[i] > input[i + 1]:
                input.pop(i + 1)
        return input[0]


def is_equal(a: list[int], b: list[int]) -> bool:
    """Returns True is every element in the list is equal"""
    if a == b:
        return True
    else:
        return False


def extend(a: list[int], b: list[int]) -> None:
    """Appends one list to another"""
    i = 0
    while i < len(b):
        a.append(b[i])
        i += 1
