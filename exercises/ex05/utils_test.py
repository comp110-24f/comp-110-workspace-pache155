"""A test of the list functions in utils.py"""

__author__ = "730741697"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_return_value() -> None:
    """only_evens should return a list containing only the even values of the input"""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(a) == [2, 4, 6, 8, 10]


def test_only_evens_behavior() -> None:
    """only_evens should not mutate the list"""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    only_evens(a)
    assert a == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_only_evens_edge_case() -> None:
    """if there are no even numbers in the list, only_evens should return an empty
    list"""
    b: list[int] = [1, 3, 5, 7, 9, 11, 13]
    assert only_evens(b) == []


def test_sub_return_value() -> None:
    """sub should return a subset list of the input (not inclusive end) based on
    indexes"""
    a: list[int] = [23, 97, 42, 69, 31, 82, 70]
    assert sub(a, 1, 6) == [97, 42, 69, 31, 82]


def test_sub_behavior() -> None:
    """sub should not modify the input"""
    a: list[int] = [23, 97, 42, 69, 31, 82, 70]
    sub(a, 1, 6)
    assert a == [23, 97, 42, 69, 31, 82, 70]


def test_sub_edge_case() -> None:
    """if the indexes are out of input range, sub should just use the whole input range"""
    a: list[int] = [23, 97, 42, 69, 31, 82, 70]
    assert sub(a, -2, 13) == [23, 97, 42, 69, 31, 82, 70]


def test_sub_edge_case_2() -> None:
    """if given an empty list, it should return an empty list"""
    b: list[int] = []
    assert sub(b, -1, 4) == []


def test_add_at_index_return_value() -> None:
    """add_at_index should return None."""
    a: list[int] = [12, 13, 14, 15, 16, 17]
    assert add_at_index(a, 14, 2) == None


def test_add_at_index_behavior() -> None:
    """add_at_index should modify the input list"""
    a: list[int] = [12, 13, 14, 15, 16, 17]
    add_at_index(a, 14, 2)
    assert a == [12, 13, 14, 14, 15, 16, 17]


def test_add_at_index_edge_case() -> None:
    """if given an index out of bounds add_at_index should return an index error"""
    b: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(b, 2, 3)
