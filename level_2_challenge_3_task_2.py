'''
This module allows for managing a list of people's profiles. Users can:
- Add a new profile to the list.

- Remove a profile from the list based on the first name (and last name 
if there are multiple first name entries).

- View all profiles in the list.

The profiles contain the person's first name, last name, age, and 
employment status.
'''


def create_profile(first_name: str,
                   last_name: str,
                   age: int,
                   employed_status: bool) -> dict:
    """
    Generates a profile for a person with their provided personal 
    details.

    Args:
        first_name (str): The individual's first name.
        last_name (str): The individual's last name.
        age (int): The individual's age.
        employed_status (bool): The individual's employment status (True
        for employed, False for not).

    Returns:
        dict: A dictionary containing the individual's profile 
        information, with keys for:
        - first_name 
        - last_name
        - age
        - employment_status
    """

    people = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "employed_status": employed_status
    }

    return people


def prompt_for_personal_details() -> dict:
    """
    Prompts the user for personal details, validates the inputs and 
    returns a dictionary of the new details.

    This function depends on 'create_profile' function to create a 
    dictionary of user details after collecting inputs for first name, 
    last name, age and employment status.

    Returns:
        dict: A dictionary containing the user's input for the first 
        name, last name, age, and employment status.

    Raises:
        ValueError:
        - If first_name or last_name contains non-alphabetic characters.
        - If non-numeric input is provided for age.
        - If invalid employment status is entered.
    """
    first_name = input("First name: ").title()
    if not first_name.isalpha():
        raise ValueError("Please only use letters in the alphabet.")

    last_name = input("Last name: ").title()
    if not last_name.isalpha():
        raise ValueError("Please only use letters in the alphabet.")

    age = input("Age: ")
    if not age.isnumeric():
        raise ValueError("Please enter an integer")
    age = int(age)

    employed_status = input("Are you employed? ")
    if employed_status.lower() == "yes":
        employed_status = True
    elif employed_status.lower() == "no":
        employed_status = False
    else:
        raise ValueError("Please type either 'yes' or 'no'.")

    new_details = create_profile(
        first_name,
        last_name,
        age,
        employed_status
    )
    return new_details


def display_details(people_profiles: list) -> None:
    """
    Displays the details of people in a list.

    Args:
        people_profiles (list): a list of dictionaries, where each 
        dictionary contains a person's profile.

    Returns:
        None
    """
    print("")
    for person in people_profiles:
        print(
            f"""First Name: {person['first_name']}
Last Name: {person['last_name']}
Age: {person['age']}
Employed: {person['employed_status']}
---------------------------------""")


def find_profiles_by_first_name(people_profiles: list[dict],
                                name_for_removal: str) -> list[dict]:
    """
    Searches for people with the specified first name in the list of 
    people details.

    Args:
        people_profiles (list[dict]): A list of dictionaries containing 
        people profiles.

        name_for_removal (str): The first name of the person to search 
        for.

    Returns:
        list[dict]: A list of dictionaries containing the first and 
        last name of people matching the specified first name.
    """
    names_found = [{"first_name": person["first_name"],
                    "last_name": person["last_name"]}
                   for person in people_profiles
                   if name_for_removal == person["first_name"]]
    return names_found


def remove_profile(people_profiles: list[dict],
                   names_found: list[dict],
                   name_for_removal: str) -> dict:
    """
    Removes an entry from the list of people details based on the 
    provided name.

    If there are multiple people with the same first name, the user 
    will be prompted to specify the last name 
    of the person to remove.

    Args:
        people_profiles (list[dict]): A list of dictionaries containing 
        people profiles.

        names_found (list[dict]): A list of dictionaries containing 
        people with the name requested for removal.

        name_for_removal (str): The first name of the person to remove.

    Returns:
        dict: The removed person's profile as a dictionary.

    Raises:
        UnboundLocalError: If no matching person is found to remove.
    """

    removed_entry = None

    # If there are multiple matches, prompt for last name to remove
    if len(names_found) > 1:
        print("")
        print("There are multiple people with that name:")
        for person in names_found:
            print(f"- {person['first_name']} {person['last_name']}")

        print("")
        last_name_for_removal = input(
            "Please enter the last name of the person you want to remove: "
        ).title()

        for num, person in enumerate(people_profiles):
            if (name_for_removal == person["first_name"] and
                    last_name_for_removal == person["last_name"]):
                removed_entry = people_profiles.pop(num)

    else:
        # If there's exactly one match, remove it
        for num, person in enumerate(people_profiles):
            if name_for_removal == person["first_name"]:
                removed_entry = people_profiles.pop(num)

    if removed_entry is None:
        raise UnboundLocalError("No matching person found to remove")

    return removed_entry


def main() -> None:
    """
    Main function that interacts with the user to manage a list of 
    people profiles. 

    It provides options for the user to:
    - Add a new profile to the list.
    - Remove a profile from the list.
    - Exit the program.

    The profiles contain information about the person's first name, 
    last name, age, and employment status.

    Returns:
        None
    """
    people_profiles = [
        {"first_name": "Jane",
         "last_name": "Doe",
         "age": 42,
         "employed_status": True},

        {"first_name": "Tom",
         "last_name": "Smith",
         "age": 18,
         "employed_status": True},

        {"first_name": "Mariam",
         "last_name": "Coulter",
         "age": 66,
         "employed_status": False},

        {"first_name": "Gregory",
         "last_name": "Tims",
         "age": 8,
         "employed_status": False}
    ]
    display_details(people_profiles)

    while True:
        action = input(
            "\nType 'Add' to add an entry to the list\n"
            "Type 'Remove' to remove an entry\n"
            "Type 'Exit' to exit the program\n\n"
        )

        if action.title() == "Add":
            try:
                print("")
                new_profile = prompt_for_personal_details()
            except ValueError as e:
                print("")
                print(e)
                continue
            people_profiles.append(new_profile)
            display_details(people_profiles)

        elif action.title() == "Remove":
            print("")
            name_for_removal = input(
                "Enter a name you would like to remove: "
            ).title()
            names_found = find_profiles_by_first_name(
                people_profiles, name_for_removal)

            try:
                remove_profile(people_profiles, names_found, name_for_removal)
            except UnboundLocalError as e:
                print("")
                print(e)
                continue

            display_details(people_profiles)

        elif action.title() == "Exit":
            break

        else:
            print("")
            print("Please enter either 'Add', 'Remove', or 'Exit'.")


if __name__ == "__main__":
    main()
