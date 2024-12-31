"""
This module defines a program for greeting pets based on their type.

It defines a function 'say_hello_to_pets' that takes a list of pet 
dictionaries and prints a greeting message for each pet depending on 
whether they are a dog or a cat.

The module also includes a 'main' function that initialises a list of 
pets and calls 'say_hello_to_pets' to display their greetings.
"""

def say_hello_to_pets(pets: list[dict[str,str]]) -> None:
    """
    Greets each pet in the provided list based on its type.

    Args:
        pets (list of dict): A list of dictionaries containing the 
        pet's name and type as strings.
                                              
    Returns:
        None: Prints the hello message based on the pet. 
    """
    greeting_map = {"dog": "woof", "cat": "meow"}
    unrecognised_pets = [
            pet for pet in pets if pet["type"] not in greeting_map
    ]

    for pet in pets:
        if pet["type"] in greeting_map:
            pet_greeting = greeting_map[pet['type']].title()
            print(f"{pet_greeting}, {pet['name']}!")

    if unrecognised_pets:
        raise AttributeError("there are unrecognised pet(s) found in the system.")

#       I know that we're supposed to raise an AttributeError but I found a nice
#       way to handle the error without it:

#       print(f"\nThe following are not in the system:")
#       for animal in unrecognised_pets:
#           print(f"- {animal['name']} ({animal['type']})")


def main() -> None:
    """
    Initializes a list of pets and calls `say_hello_to_pets` to greet them.
 
    Args:
        None

    Returns:
        None
    """
    animals = [
            { "name": "Fluffy", "type": "dog" },
            { "name": "Parsley", "type": "dog" },
            { "name": "Ginger", "type": "cat" },
            { "name": "Poppet", "type": "cow" },
            { "name": "Biscuit", "type": "cat" }
    ]

    try:
        say_hello_to_pets(animals)
    except AttributeError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()

