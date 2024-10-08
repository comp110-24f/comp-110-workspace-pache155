"""EX03 - Wordle - An attepmt at programming wordle."""

__author__ = "730741697"


def input_guess(secret_word_len: int) -> str:
    """Checks if the inputted word is the proper length"""
    word = str(input(f"Enter a {secret_word_len} character word: "))
    while len(word) != secret_word_len:
        word = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if a character is in the inputted word"""
    assert len(char_guess) == 1
    index: int = -1
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        else:
            index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Converts the matching and non matching letters into a string of emojis"""
    assert len(guess) == len(secret)
    answer = ""
    index1 = 0
    First = contains_char(secret_word=secret, char_guess=guess[index1])
    Final: list[str] = []
    if First == True:
        if secret[index1] == guess[index1]:
            str1 = GREEN_BOX
        else:
            str1 = YELLOW_BOX
    else:
        str1 = WHITE_BOX
    answer = str1
    while index1 < len(secret) - 1:
        index1 += 1
        if contains_char(secret_word=secret, char_guess=guess[index1]) == True:
            if secret[index1] == guess[index1]:
                str2 = GREEN_BOX
                answer += str2
            else:
                str2 = YELLOW_BOX
                answer += str2
        else:
            str2 = WHITE_BOX
            answer += str2
    return answer


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    print(f"=== Turn {turn}/6 ===")
    word = input_guess(secret_word_len=len(secret))
    print(emojified(guess=word, secret=secret))
    if word == secret:
        print(f"\nYou won in {turn}/6 turns!")
    else:
        while turn < 6:
            turn += 1
            print(f"\n=== Turn {turn}/6 ===")
            word = input_guess(secret_word_len=len(secret))
            print(emojified(guess=word, secret=secret))
            if word == secret:
                print(f"\nYou won in {turn}/6 turns!")
                turn = 20
        if turn != 20:
            print("\nX/6 - Sorry, try again tomorrow!")
        else:
            print("")


# I had trouble figuring out how many times the loop would go through and has it as
# I had turn <= 6 before and that made if end at 7/6 rounds
# Took me a while to figure out how to properly concatenate the strings

if __name__ == "__main__":
    main(secret="codes")
