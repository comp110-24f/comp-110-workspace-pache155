"""CQ04-concatenation-The First Step"""

__author__ = "730741697"


def concat(str1: str, str2: str) -> str:
    """Returns the concatenation of two strings"""
    return str1 + str2


word1 = "happy"
word2 = "tuesday"


def main() -> None:
    print(concat(word1, word2))


if __name__ == "__main__":
    main()
