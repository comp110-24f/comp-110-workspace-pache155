"""A test of the find_and_remove_max"""

__author__ = "730741697"

from CQs.cq07.find_max import find_and_remove_max


def test_return_expected_value() -> None:
    """find_and_remove_max should return the greatest element"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    assert find_and_remove_max(a) == 6


def test_mutates_list() -> None:
    """find_and_remove_max should mutate the list"""
    a: list[int] = [1, 2, 3, 4, 5, 6]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 4, 5]


def test_edge_case() -> None:
    """find_and_remove_max on an empty list should return -1"""
    assert find_and_remove_max([]) == -1
