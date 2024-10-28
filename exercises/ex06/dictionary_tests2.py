"""A test of the dictionary utils"""

__author__ = "730741697"

def invert(a: dict[str, str]) -> dict[str, str]:
    """inverts the keys and outputs of a dictionary"""
    x = ""
    idx = 0
    b: list[str] = []
    c: dict[str, str] = {}
    for i in a:
        b.append(a[i])
    for idx in range(len(b) - 1):
        if b[idx] == b[idx + 1]:
            raise KeyError("key error in output")
    for i in a:
        x = a[i]
        c[x] = i
    return c


def favorite_color(color: dict[str, str]) -> str:
    """Determines what is the most popular color in a dictionary of favorit colors"""
    b: list[str] = []
    d: list[int] = []
    greatest = 0
    idx = 0
    count = 0
    i = 0
    x = 1
    for person in color:
        b.append(color[person])
    while idx < (len(b)):
        for i in range(len(b)):
            if b[idx] == b[i]:
                count += 1
            else:
                count = count
        d.append(count)
        count = 0
        idx += 1
    while i < len(b):
        while x > i and x < len(b):
            if b[i] == b[x]:
                b.pop(i)
                d.pop(i)
            x += 1
        i += 1
        x = i + 1
    assert len(d) == len(b)
    for i in range(len(d)):
        if d[i] >= greatest:
            greatest = d[i]
        else:
            greatest = greatest
    for i in range(len(d)):
        if d[i] == greatest:
            return b[i]


def count(b: list[str]) -> dict[str, int]:
    """Counts each item in a list and produces a dictionary"""
    c: dict[str, int] = {}
    d: list[int] = []
    idx = 0
    count = 0
    i = 0
    x = 1
    while idx < (len(b)):
        for i in range(len(b)):
            if b[idx] == b[i]:
                count += 1
            else:
                count = count
        d.append(count)
        count = 0
        idx += 1
    while i < len(b):
        while x > i and x < len(b):
            if b[i] == b[x]:
                b.pop(i)
                d.pop(i)
            x += 1
        i += 1
        x = i + 1
    assert len(d) == len(b)
    for i in range(len(b)):
        c[b[i]] = d[i]
    return c


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """"""
    b: str = ""
    c: list[str] = []
    d: str = ""
    e: list[str] = []
    f: dict[str, list[str]] = {}
    x = 1
    n = 0
    y = 0
    z = 0
    idx = 1
    for i in range(len(a)):
        b = a[i]
        c.append(b[0].lower())
    while n < len(c):
        while x > n and x < len(c):
            if c[n] == c[x]:
                c.pop(n)
            x += 1
        n += 1
        x = n + 1
    while idx < len(c):
        if c[0] == c[idx]:
            c.pop(idx)
            idx += 1
        else:
            idx += 1
    while z < len(c):
        while y < len(a):
            d = a[y]
            if d[0].lower() == c[z]:
                e.append(d)
            y += 1
        for i in range(len(e)):
            f[c[z]] = e[]
        z += 1
        for i in range(len(e)):
            e.pop(i)
    return f


def test_invert_expected_value() -> None:
    """find_and_remove_max should return the greatest element"""
    a: dict[str, str] = {"apple": "cat"}
    assert invert(a) == {"cat": "apple"}


def test_color_expected_valued2() -> None:
    """find_and_remove_max should return the greatest element"""
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
