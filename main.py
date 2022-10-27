"""
CP1404 - Guessing Game for review and refactor
Some of this is "good" code, but some things are intentionally poor
This is for a code review and refactoring exercise
"""
import math
import random

DEFAULT_LOW = 1
DEFAULT_HIGH = 10


def main():
    """Menu-driven guessing game with option to change high limit."""
    low = DEFAULT_LOW
    high = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input("(P)lay, (S)et limit, (H)igh scores, (Q)uit: ").upper()
    while choice != "Q":
        if choice == "P":
            play(low, high)
            number_of_games += 1
        elif choice == "S":
            high = set_limit(low)
        elif choice == "H":
            high_scores()
        else:
            print("Invalid choice")
        choice = input("(P)lay, (S)et limit, (H)igh scores, (Q)uit: ").upper()
    print(f"Thanks for playing ({number_of_games} times)!")


def score_save(number_of_guesses, low, high):
    """Save score to scores.txt with range"""
    with open("scores.txt", "a", encoding="utf-8-sig") as outfile:
        print(f"{number_of_guesses}|{high - low + 1}", file=outfile)


def play(low, high):
    """Play guessing game using current low and high values."""
    secret = random.randint(low, high)
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret:
        number_of_guesses += 1
        if guess < secret:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses.")
    if good_score(number_of_guesses, high - low + 1) is True:
        print("Good guessing!")
    else:
        pass
    choice = input("Do you want to save your score? (y/N) ")
    if choice.upper() == "Y":
        score_save(number_of_guesses, low, high)
        return
    print("Fine then.")


def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    while new_high <= low:
        print("Higher!")
        new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    return new_high


def get_valid_number(prompt):
    """Get valid number from user input, checks for errors and returns the number"""
    number = 0
    is_valid = False
    while is_valid is False:
        try:
            number = int(input(prompt))
            is_valid = True
        except ValueError:
            print("Invalid number")
    return number


def good_score(number_of_guesses, range_):
    if number_of_guesses <= math.ceil(math.log2(range_)):
        return True


def high_scores():
    """opens file, processes file contents, adds contents to scores list and
        prints the list with string formatting"""
    scores = []
    with open("scores.txt") as in_file:
        for line in in_file:
            line = line.split("|")
            scores.append((int(line[0]), int(line[1])))
    scores.sort()
    for score in scores:
        marker = "!" if good_score(score[0], score[1]) else ""
        print(f"{score[0]} ({score[1]}) {marker}")


main()
