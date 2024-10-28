"""A test of the dictionary utils"""

__author__ = "730741697"

from exercises.ex06.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


def test_invert_expected_value() -> None:
    """invert should return a dictionary with the reverse keys of the input dictionary"""
    a: dict[str, str] = {"apple": "cat"}
    assert invert(a) == {"cat": "apple"}


def test_color_expected_valued2() -> None:
    """favorite_color should return the first color mentioned if all colors have
    equal count"""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "orange"}
    assert favorite_color(a) == "yellow"


def test_color_expected_value() -> None:
    """find_and_remove_max should return the greatest element"""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_color_expected_value3() -> None:
    """find_and_remove_max should return the greatest element"""
    a: dict[str, str] = {
        "Marc": "yellow",
        "Ezri": "blue",
        "Kris": "blue",
        "a": "muave",
        "b": "muave",
        "c": "tangerine",
        "d": "lavender",
    }
    assert favorite_color(a) == "blue"


def test_color_expected_value4() -> None:
    """find_and_remove_max should return the greatest element"""
    a: dict[str, str] = {
        "Marc": "yellow",
    }
    assert favorite_color(a) == "yellow"


def test_count_value() -> None:
    """"""
    a: list[str] = [
        "p",
        "p",
        "p",
        "p",
        "p",
        "p",
        "p",
        "l",
        "l",
        "l",
        "l",
        "l",
        "l",
        "m",
    ]
    assert count(a) == {"p": 7, "l": 6, "m": 1}


def test_alphabetizer_expected_value() -> None:
    """find_and_remove_max should return the greatest element"""
    a: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(a) == {
        "c": ["cat", "car"],
        "a": ["apple", "angry"],
        "b": ["boy", "bad"],
    }


def test_alphabetizer_expected_value2() -> None:
    """find_and_remove_max should return the greatest element"""
    a: list[str] = ["cat", "car"]
    assert alphabetizer(a) == {
        "c": ["cat", "car"],
    }


def test_update_attendance_expected_value() -> None:
    """"""
    a: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    b: str = "Tuesday"
    c: str = "Vrinda"
    update_attendance(a, b, c)
    assert a == {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
        "Wednesday": ["Kaleb"],
    }
