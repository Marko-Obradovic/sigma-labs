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

def get_guess(previous_guess: int, min_bound: int, max_bound: int) -> int:
    guess = input(f"Guess a number between {min_bound} and {max_bound}: ")
    if not guess.isnumeric():
        raise(ValueError("Please enter an integer"))
    guess = int(guess)
    if guess == previous_guess:
        raise(ValueError("Same as previous answer. Continuing..."))
    elif guess < 0 or guess > 100:
        raise(ValueError("Please enter a value between 0 and 100"))
    return guess


def check_guess(guess: int, answer: int) -> str:
    if guess < answer:
        return "Higher..."
    elif guess > answer:
        return "Lower..."
    else:
        return "You Won!"


def run_game(min_bound: int, max_bound: int) -> str:
    answer = random.randint(0, 100)
    previous_guess = float("inf")
    print(answer)
    tries = 0

    while True:
        try:
            guess = get_guess(previous_guess, min_bound, max_bound)
        except ValueError as e:
            print(e)
            continue
        result = check_guess(guess, answer)
        print(result)
        tries += 1
        previous_guess = guess
        if guess == answer:
            break

    return f"Attempts: {tries}"


def main() -> None:
    min_bound = 0
    max_bound = 100
    print(run_game(min_bound, max_bound))

if __name__ == "__main__":
    main()

