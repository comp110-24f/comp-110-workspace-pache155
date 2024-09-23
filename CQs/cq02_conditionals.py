"""A number guessing game"""

__author__ = "730741697"


def guess_a_number() -> None:
    """Says if the guess is right or wrong"""
    x = input("Guess a number: ")
    secret: int = 7
    print("Your guess was " + str(x))
    if int(x) == int(secret):
        print("You got it!")
    elif int(x) < int(secret):
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(x) > int(secret):
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
