"""Mutating functions"""

__author__ = "730741697"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], b: int) -> None:
    """appends the int parameter onto the list parameter"""
    a.append(b)


def double(a: list[int]) -> None:
    index: int = 0
    """Multiplies every element in the list by 2"""
    while index < len(a):
        a[index] = a[index] * 2
        index += 1


double(list_2)

print(list_1)
print(list_2)
# list_1 will remain the same
# list_2 will be doubled
