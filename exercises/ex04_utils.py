"""A bunch of list functions"""

__author__ = "730741697"


def all(a: list[int], b: int) -> bool:
    """Indicates if whether or not a list is made up of one given integer"""
    i = 0
    c = 0
    if len(a) == 0:
        return False
    else:
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
        return input[i]


def is_equal(c: list[int], d: list[int]) -> bool:
    """Returns True is every element in the list is equal"""
    if c == d:
        return True
    else:
        return False


def extend(e: list[int], f: list[int]) -> None:
    """Appends one list to another"""
    i = 0
    while i < len(f):
        e.append(f[i])
        i += 1
