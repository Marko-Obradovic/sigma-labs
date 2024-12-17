"""Gives user a choice between two options:
1. Create an obfuscated username based on a name
2. Generate a random username
"""

import sys

import random
import functools
import string
from typing import Callable, Any

import styling

def input_error_handling(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper() -> Any:
        while True:
            try:
                return func()
            except KeyboardInterrupt:
                print("\n\nProgram Stopped")
                sys.exit()
            except ValueError:
                print(styling.notification("Please enter either 1 or 2!"))
    return wrapper


@input_error_handling
def get_username_creation_method() -> int:
    welcome_message = "Welcome to the username creator. Please choose an option: "
    display_choices = "1. Create based on a name\n2. Generate a random username"
    username_creation_method = int(input(f"\n{welcome_message}\n\n{display_choices}\n\n-> "))
    return username_creation_method


@input_error_handling
def get_name_and_surname() -> dict:
    user_info: dict = {}
    name = str(input('\nPlease enter your name: ')).lower()
    surname = str(input('Please enter your surname: ')).lower()
    user_info["name"] = name
    user_info["surname"] = surname
    return user_info


def reverse_name(name_input: str) -> str:
    name_chars: list = list(name_input)
    name_chars.reverse()
    return ''.join(name_chars)


def intersperse_name(name_input: str, surname_input: str) -> list[str]:
    interspersed_char_list = []
    for index, char in enumerate(name_input):
        interspersed_char_list.append(char)
        if index < len(surname_input):
            interspersed_char_list.append(surname_input[index])
        if index == len(name_input) - 1:
            for remaining_char in surname_input[index + 1:]:
                interspersed_char_list.append(remaining_char)
    return interspersed_char_list


def random_name_generator(letters_and_numbers: list[str]) -> str:
    random_name = ''.join(random.choices(letters_and_numbers, k=random.randint(3, 9)))
    return random_name


def format_name(char_list: list[str], name_input: str) -> str:
    char_list.insert(len(name_input), ' ')
    return ''.join(char_list).title()


def letters_and_numbers_list() -> list[str]:
    letters: list[str] = list(string.ascii_letters)
    numbers: list[str] = [str(number) for number in range(10)]
    letters_and_numbers: list[str] = letters + numbers
    return letters_and_numbers


def main() -> None:
    chosen_method: int = get_username_creation_method()

    if chosen_method == 1:
        name_and_surname = get_name_and_surname()
        name = name_and_surname["name"]
        surname = name_and_surname["surname"]

    elif chosen_method == 2:
        name = random_name_generator(letters_and_numbers_list())
        surname = random_name_generator(letters_and_numbers_list())

    interspersed_name = intersperse_name(reverse_name(name), surname)
    print(f'\nYour username is: {format_name(interspersed_name, name_input = name)}\n')


if __name__ == "__main__":
    main()
