"""Three list functions"""

__author__ = "730741697"


def get_first(input: list[str]) -> str:
    """returns the first element of a list of strings"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """removes the first element of a list of strings"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Removes and returns the first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element
