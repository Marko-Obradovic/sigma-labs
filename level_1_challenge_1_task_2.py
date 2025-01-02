'''This program checks if the user's name is in the list of authorised names and greets them if it is.
It will prompt the user for their first name and respond accordingly.
'''

authorised_names = {"Alice", "Bob"}


def get_name() -> str:
    name: str = input("What's your first name?: ")
    return name.title().strip()


def greet_if_authorised(name: str, authorised_names_list: set) -> str:
    if name in authorised_names_list:
        return f"Hello {name}!"
    return "Sorry... You're not authorised to be greeted!"


def main(message: str) -> None:
    print(message)


if __name__ == "__main__":
    main(greet_if_authorised(get_name(), authorised_names))
