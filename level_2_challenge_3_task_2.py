'''
'''

import sys

import functools
from collections.abc import Callable

import styling

def generate_profile(first_name: str, last_name: str, age: int, employed_status: bool):
    people = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "employed_status": employed_status
            }
    return people


def get_new_details() -> dict:
    first_name = (input("First name: "))
    last_name = (input("Last name: "))
    age = (input("Age: "))
    employed_status = (input("Are you employed? "))

    new_details = generate_profile(first_name, last_name, age, employed_status)

    return new_details


def display_details(people_details: dict) -> None:
    for person in people_details:
        for i in person.items():
            print(f"{i[0]}: {i[-1]}")
        print("----------------------------")


def prompt_action() -> str:
    choice = str(input(f"\nType 'Add' to add an entry to the list\nType 'Remove' to remove an entry\nType 'Exit' to exit the program\n\n"))
    return choice


def add_entry_to_list():
    """Asks 
    """
    new_first_name = input("enter first name: ")
    new_last_name = input("enter last name: ")
    new_age = input("enter age: ")
    new_employed_status = input("enter employment status: ")

    new_value_groups = [new_first_name, new_last_name, new_age, new_employed_status]

    return new_value_groups


def find_names(people_details: list[dict], name_for_removal: str) -> list[tuple[str]]:
    names_found = []
    for num, person in enumerate(people_details):
        if name_for_removal == person["first_name"]:
            first_and_last_name = (person["first_name"], person["last_name"])
            names_found.append(first_and_last_name)
    return names_found


def remove_entry_from_list(people_details: list[dict]) -> ...:
    name_for_removal = input("Enter a name you would like to remove: ")

    names_found = find_names(people_details, name_for_removal)

    if len(names_found) > 1:
        print("There are multiple people with that name:")
        for name in names_found:
            print(f"{name[0]} {name[-1]}")
        last_name_for_removal = input("Please enter the last name of the person you want to remove: ")

        for num, person in enumerate(people_details):
            if name_for_removal == person["first_name"] and last_name_for_removal == person["last_name"]:
                removed_entry = people_details.pop(num)

    else:
        for num, person in enumerate(people_details):
            if name_for_removal == person["first_name"]:
                removed_entry = people_details.pop(num)

    return removed_entry


def main() -> None:
    people = [
        {"first_name": "Jane", "last_name": "Doe", "age": 42, "employed": True},
        {"first_name": "Jane", "last_name": "Test", "age": 100000, "employed": True},
        {"first_name": "Tom", "last_name": "Smith", "age": 18, "employed": True},
        {"first_name": "Mariam", "last_name": "Coulter", "age": 66, "employed": False},
        {"first_name": "Gregory", "last_name": "Tims", "age": 8, "employed": False}
        ]
    display_details(people)

    while True:
        try:
            action = prompt_action()
        except ValueError as e:
            print(e)
            continue

        if action == "Add":
            new_profile = get_new_details()
            people.append(new_profile)
            display_details(people)

        elif action == "Remove":
            removed_entry = remove_entry_from_list(people)
            display_details(people)

        elif action == "Exit":
            break


if __name__ == "__main__":
    main()
