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


if __name__ == "__main__":
    b: dict[str, str] = {
        "Marc": "yellow",
        "Ezri": "blue",
        "Kris": "blue",
        "a": "muave",
        "b": "muave",
        "c": "tangerine",
        "d": "lavender",
    }
    print(favorite_color(b))
