"""My challenge question in COMP110!"""

__author__ = "730741697"


def mimic(message: str) -> str:
    """A mimic funstion defintion, returns what you type"""
    return message


def main() -> None:
    """Prints out the results of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
