"""CQ04-Coordinates"""

__author__ = "730741697"


def get_coords(xs: str, ys: str) -> None:
    """Prints the formatted pairs of each character in the two input strings"""
    index1: int = 0
    index2: int = 0
    while index1 < len(xs):
        while index2 < len(ys):
            if not index1 < len(xs):
                break
            print("(" + xs[index1] + ", " + ys[index2] + ")")
            if len(ys) != index2 + 1:
                index2 += 1
            elif len(ys) == index2 + 1:
                index1 += 1
                index2 = 0


# For a while my nested loop was ignoring my outer loop and I used a break to remedy it
# It also took me a bit to grasp the loop logic
