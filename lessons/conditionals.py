"""Practice with conditionals"""


def less_than_10(num: int) -> bool:
    """Tells me if a number is less than 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("Have a nice day!")


less_than_10(num=7)


def should_i_eat(hungry: bool) -> None:
    """fwe"""
    if hungry:
        print("Go eat something.")
    else:
        print("Go do work")
    print("I'm proud of you <3")  # either way be proud of yourself


def check_first_letter(word: str, letter: str) -> str:
    """fewfwegew"""
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="s")
