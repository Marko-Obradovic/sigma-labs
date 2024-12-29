'''
'''

import sys

import functools
from collections.abc import Callable

def generate_profile(first_name: str, last_name: str, age: int, employed_status: bool):
    people = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "employed_status": employed_status
            }
    return people


def get_new_details() -> dict:
    first_name = (input("First name: ")).title()

    last_name = (input("Last name: ")).title()

    age = (input("Age: "))
    if not age.isnumeric():
        raise(ValueError("Please enter an integer"))
    age = int(age)

    employed_status = (input("Are you employed? "))
    if employed_status.lower() == "yes":
        employed_status = True
    elif employed_status.lower() == "no":
        employed_status = False
    else:
        raise(ValueError("Please type either 'yes' or 'no'."))

    new_details = generate_profile(first_name, last_name, age, employed_status)

    return new_details


def display_details(people_details: dict) -> None:
    for person in people_details:
        print(
        f"""First Name: {person['first_name']}
Last Name: {person['last_name']}
Age: {person['age']}
Employed: {person['employed_status']}
---------------------------------""")


def find_names(people_details: list[dict], name_for_removal: str) -> list[tuple[str]]:
    names_found = [{"first_name":person["first_name"], "last_name":person["last_name"]}
                   for num, person in enumerate(people_details)
                   if name_for_removal == person["first_name"]]
    return names_found


def remove_entry(people_details: list[dict], names_found: list[tuple[str]], name_for_removal: str) -> ...:
    # If there are multiple matches, prompt for last name to remove
    if len(names_found) > 1:
        print("There are multiple people with that name:")
        for person in names_found:
            print(f"{person['first_name']} {person['last_name']}")
        last_name_for_removal = input("Please enter the last name of the person you want to remove: ").title()

        for num, person in enumerate(people_details):
            if name_for_removal == person["first_name"] and last_name_for_removal == person["last_name"]:
                removed_entry = people_details.pop(num)
    
    else:
        # If there's exactly one match, remove it
        for num, person in enumerate(people_details):
            if name_for_removal == person["first_name"]:
                removed_entry = people_details.pop(num)

    return removed_entry


def main() -> None:
    people = [
        {"first_name": "Jane", "last_name": "Doe", "age": 42, "employed_status": True},
        {"first_name": "Jane", "last_name": "Test", "age": 100000, "employed_status": True},
        {"first_name": "Tom", "last_name": "Smith", "age": 18, "employed_status": True},
        {"first_name": "Mariam", "last_name": "Coulter", "age": 66, "employed_status": False},
        {"first_name": "Gregory", "last_name": "Tims", "age": 8, "employed_status": False}
        ]
    display_details(people)

    while True:
        try:
            action = str(input(f"\nType 'Add' to add an entry to the list\nType 'Remove' to remove an entry\nType 'Exit' to exit the program\n\n"))
        except ValueError as value_error:
            print(value_error)
            continue

        if action == "Add":
            try:
                new_profile = get_new_details()
            except ValueError as e:
                print(e)
                continue
            people.append(new_profile)
            display_details(people)

        elif action == "Remove":
            name_for_removal = input("Enter a name you would like to remove: ").title()
            names_found = find_names(people, name_for_removal)
            try:
                removed_entry = remove_entry(people, names_found, name_for_removal)
            except UnboundLocalError:
                print("Name not found.")
                continue
            display_details(people)

        elif action == "Exit":
            break


if __name__ == "__main__":
    main()
