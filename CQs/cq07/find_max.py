"""A function that finds and rmoves the largest interger in a list"""

__author__ = "730741697"


def find_and_remove_max(input: list[int]) -> int:
    """Will find and return the largest number in a list and remove that number from the list"""
    i = 0
    i2 = 0
    max = 0
    if len(input) == 0:
        return -1
    else:
        while i < len(input):
            if input[i] > max:
                max = input[i]
                i += 1
            else:
                max = max
                i += 1
        while i2 < len(input):
            if input[i2] == max:
                input.pop(i2)
            else:
                i2 += 1
        return max
