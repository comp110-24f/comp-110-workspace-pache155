"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730741697"


def input_word() -> str:
    """Asks for a 5 letter word"""
    word = str(input("Enter a 5-character word: "))
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


def input_letter() -> str:
    """Asks for a letter"""
    letter = str(input("Enter a single character: "))
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


# I forgot to have the if statements on the same line so if the first if wasnt true, it would exit out
# of the program completely lol
# I thought we were using while loops at first
# hard coding did not come to me AT ALL at first
# I don't need a command for it the index doesn't match the letter lol
def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is in the word"""
    count: int = 0
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
