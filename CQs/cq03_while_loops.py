"""Counts the number of a certain character in a phrase"""

__author__ = "730741697"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of a certain character in a phrase"""
    count: int = 0
    index: int = 0
    while index < int(len(phrase)):
        if (phrase[index]) == search_char:
            count = count + 1
            index = index + 1
        elif (phrase[index]) != search_char:
            count = count
            index = index + 1
    return count


# not printing? Index out of range? I forgot to quit my REPL which was causing the problems
