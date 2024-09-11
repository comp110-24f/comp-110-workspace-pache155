"""A program that calculates the amount of food and tea needed for a tea party based on the number of guests"""

__author__ = "730741697"


def main_planner(guests: int) -> None:
    """Determines the amount of guests at the tea party"""
    print(
        "A cozy tea party for "
        + str(guests)
        + " people!"
        + "\n Tea bags: "
        + str(tea_bags(people=guests))
        + "\n Treats: "
        + str(treats(people=guests))
        + "\n Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# use \n for a new line and + to connect strings, make the functions called a string before being printed.


def tea_bags(people: int) -> int:
    """Returns the amount of tea bags needed based on the amount of guests"""
    return people * 2


# didn't work at first, I forgot to call the function


def treats(people: int) -> int:
    """Determines the amount of treats each guest will eat"""
    return int(tea_bags(people=people) * 1.5)


# was't printing in REPL at first but fixed itself, trailhead issue?


def cost(tea_count: int, treat_count: int) -> float:
    """Returns total cost of supplies"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
