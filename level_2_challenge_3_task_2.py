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
            except ValueError:
                print(styling.notification("Invalid input. Please enter a valid number."))
                continue
    return wrapper


def generate_profiles(attributes: list[str], value_groups: zip):
    people: list[dict] = [
            {attribute:value for attribute, value in zip(attributes, values)}
            for values in value_groups
            ]
    return people


def display_details(people_details: dict) -> None:
    format_details: list = 
    for person in people_details:
        for i in person.items():
            print(f"{i[0]}: {i[-1]}")
        print("-------------")


@error_handling
def prompt_action() -> str:
    choice = str(input(f"\nType 'Add' to add an entry to the list\nType 'Remove' to remove an entry\n\n"))
    return choice


@error_handling
def get_user_details(detail):
    user_details = str(input(f"{detail}: "))
    return user_details


def add_entry_to_list():
    new_first_name = input("enter first name: ")
    new_last_name = input("enter last name: ")
    new_age = input("enter age: ")
    new_employed_status = input("enter employment status: ")
    new_value_groups = [new_first_name, new_last_name, new_age, new_employed_status]
    return new_value_groups

def remove_entry_from_list(people_details: list[dict]):
    pass


attributes: list[str] = ["First name", "Last name", "Age", "Employed"]

first_names: list[str] = ["Jane", "Tom", "Mariam", "Gregory"]
last_names: list[str] = ["Doe", "Smith", "Coulter", "Tims"]
ages: list[int] = [42, 18, 66, 8]
employed_status: list[bool] = [True, True, False, False]

value_groups = zip(first_names, last_names, ages, employed_status)

people = generate_profiles(attributes, value_groups)

def main() -> None:
    display_details(people)
    action = prompt_action()
    if action == "Add":
        new_values = add_entry_to_list()
        first_names.append(new_values[0])
        last_names.append(new_values[1])
        ages.append(new_values[2])
        employed_status.append(new_values[3])
        people_two = generate_profiles(attributes, value_groups)
        print(display_details(people_two))
    elif action == "Remove":
#        remove_entry_from_list()
        print("removal successful")

if __name__ == "__main__":
    main()
