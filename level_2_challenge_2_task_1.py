import sys

import random
import functools
from collections.abc import Callable

import styling



def error_handling(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper() -> :
        while True:
            try:
                return func()
            except KeyboardInterrupt:
                print("\n\nProgram stopped.")
                sys.exit()
            except ValueError:
                print(styling.notification("Invalid input. Please enter a valid number."))
                continue
    return wrapper

@error_handling
def user_guess() -> int:
    return int(input("Guess a number between 0 and 100: "))

def main() -> None:
    answer: int = random.randint(0, 100) 
    prev_guess: int = 0
    tries: int = 0
    guess: int = 0
    while guess != answer:
        guess: int = user_guess()
        tries += 1
        if guess == prev_guess:
            print('\nSame as previous answer. Continuing...\n')
            continue
        elif guess < answer:
            print('\nHigher...\n')
        elif guess > answer:
            print('\nLower...\n')
        elif guess == answer:
            print('\nYou Won!\n')
            break
        prev_guess: int = guess
    print(f"Attempts: {tries}")

if __name__ == '__main__':
    main()
