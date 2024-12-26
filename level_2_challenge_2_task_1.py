"""This program is a number-guessing game.

In this game, the user tries to guess a randomly generated secret 
number between 0 and 100. 

The user will be prompted to enter a guess and will receive feedback 
on whether to guess higher or lower until they find the correct number.
"""

import sys

import random
import functools
from collections.abc import Callable

import styling

def error_handling(func: Callable[[], int]) -> Callable[[], int]:
    @functools.wraps(func)
    def wrapper() -> int:
        while True:
            try:
                return func()
            except KeyboardInterrupt:
                print("")
                print(styling.notification("Program Stopped"))
                sys.exit()
            except ValueError:
                print(styling.notification("Invalid input. Please enter a valid number."))
                continue
    return wrapper


@error_handling
def prompt_guess() -> int:
    return int(input("Guess a number between 0 and 100: "))


def check_guess() -> str:
    answer: int = random.randint(0, 100)
    previous_guess: int = 0
    tries: int = 0

    while True:
        guess: int = prompt_guess()
        if guess == previous_guess:
            print(styling.notification("Same as previous answer. Continuing..."))
            continue
        elif guess < 0 or guess > 100:
            print(styling.notification("Please enter a value between 0 and 100"))
            continue
        tries += 1
        if guess < answer:
            print("Higher...")
        elif guess > answer:
            print("Lower...")
        elif guess == answer:
            print("You Won!")
            break
        previous_guess = guess

    return f"Attempts: {tries}"


def main() -> None:
    print(check_guess())

if __name__ == '__main__':
    main()
