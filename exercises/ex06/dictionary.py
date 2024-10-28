"""Dictionary utility functions"""

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
    """Determines what is the most popular color in a dictionary of favorite colors"""
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


# went about this the completely wrong way at first. Tried to make a dict, figured out it was easier
# to just use 2 identical lists


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
    """Groups strings in a list alphabetically"""
    b: str = ""
    c: list[str] = []
    d: str = ""
    f: dict[str, list[str]] = {}
    x = 1
    n = 0
    y = 0
    p = 0
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
    for p in range(len(c)):
        f[c[p]] = []
    for t in f:
        y = 0
        while y < len(a):
            d = a[y]
            if d[0].lower() == t:
                f[t].append(d)
            y += 1
    return f


# Took me a bit to figure out how to correct the output for each key. Instead of making a list for each key
# you just append the value onto the appropriate key.


def update_attendance(
    attendence_log: dict[str, list[str]], day: str, student: str
) -> None:
    """"""
    if day in attendence_log:
        attendence_log[day].append(student)
    if day not in attendence_log:
        attendence_log[day] = [student]
    return None
