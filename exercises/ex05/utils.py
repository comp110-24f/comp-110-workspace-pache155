"""list functions"""

__author__ = "730741697"


def only_evens(a: list[int]) -> list[int]:
    """returns only the even elements in a list"""
    b: list[int] = []
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            b.append(a[i])
            i += 1
        else:
            i += 1
    return b


def sub(a: list[int], start: int, end: int) -> list[int]:
    """displays the list to the indexes of the two entered integers"""
    i = 0
    b: list[int] = []
    if start < 0:
        start = 0
    if end > len(a):
        end = len(a)
    i = start
    while i >= start and i < end:
        b.append(a[i])
        i += 1
    return b


def add_at_index(a: list[int], add1: int, addindex: int) -> None:
    """Adds an element at a list index"""
    i = 0
    b: list[int] = []
    if addindex < 0 or addindex > len(a):
        raise IndexError("Index is out of bounds for the input list")
    a.append(0)
    while i < addindex:
        b.append(a[i])
        i += 1
    b.append(add1)
    while i < len(a):
        b.append(a[i])
        i += 1
    while len(a) > 0:
        a.pop(0)
    for i in b:
        a.append(i)
    a.pop(len(a) - 1)


# for add_at_index I went through several attempts programming it. First with
# altering only the b and setting a = b at the end which did not work
# I then tried to use a loop to shift each item up in a individually
# without the use of any b but this lead to repeating values in the list
# eventually looking at my other working functions I decided to go more
# like I did with the second one and just start appending each value into
# a new list instead of modifiying the current one too much.
# with a loop it was easy to copy the new list onto the original input
# and mutate the input.
