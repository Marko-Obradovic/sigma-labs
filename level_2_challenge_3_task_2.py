'''
'''

import sys

import functools
from collections.abc import Callable

import styling 


def error_handling(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper():
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


people: list[dict] = [
        {"First name": "Jane", "Last name": "Doe", "Age": 42, "Employed": True},
        {"First name": "Tom", "Last name": "Smith", "Age": 18, "Employed": True},
        {"First name": "Mariam", "Last name": "Coulter", "Age": 66, "Employed": False},
        {"First name": "Gregory", "Last name": "Tims", "Age": 8, "Employed": False}
        ]


def display_details(people_details: dict) -> str:
    for person in people_details:
        for i in person.items():
            print(f"{i[0]}: {i[-1]}")
        print("-------------")

@error_handling
def prompt_action() -> str:
    return str(input(f"\nType 'Add' to add an entry to the list\nType 'Remove' to remove an entry\n\n"))


def main() -> None:
    display_details(people)
    prompt_action()

if __name__ == "__main__":
    main()
