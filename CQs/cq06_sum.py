"""Summing the elements of a list using different loops"""

__author__ = "730741697"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all the elements in a list"""
    sum: float = 0.0
    while len(vals) > 0:
        sum += vals[0]
        vals.pop(0)
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all the elements in a list"""
    sum: float = 0.0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all the elements in a list"""
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum
