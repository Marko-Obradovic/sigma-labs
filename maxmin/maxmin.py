"""
This module contains a program to collect a list of numbers and 
find the maximum and minimum values in that list. 
"""


def get_numbers() -> list[int]:
    """
    Collects a list of integers from the user. The user is prompted to enter numbers
    continuously until they type 'stop'. 

    Returns:
        list[int]: A list of integers entered by the user.

    Raises:
        ValueError: If the user inputs anything other than a valid number or 'stop'.
    """
    print("Keep entering numbers to create a list of numbers.")
    print("Type 'stop' to stop adding numbers.\n")
    numbers = []
    while True:
        number = input("-> ")

        if number.lower() == "stop":
            break

        if not number.lstrip('-').isnumeric():
            raise ValueError("Please enter a valid number")

        number = int(number)

        numbers.append(number)
    return numbers


def find_maxmin(numbers: list[int]) -> tuple[int, int]:
    """
    Finds the minimum and maximum values in a list of integers.

    Args:
        numbers[list[int]]: A list of integers.

    Returns:
        tuple[int, int]: A tuple containing the minimum value followed by the maximum value.

    Example:
        >>> print(find_maxmin([1, 2, 3]))
        (1, 3)

    """
    lowest = float("inf")
    highest = float("-inf")

    for num in numbers:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num

    return (lowest, highest)


def main() -> None:
    """
    This function prompts the user to enter numbers using the 
    get_numbers() function and then calls find_maxmin() to find
    the lowest and highest values in the entered list. 
    The results are then printed to the console.

    This function continuously runs the program until valid input is received.
    """
    while True:
        try:
            numbers = get_numbers()
            break
        except ValueError as e:
            print(f"\n#----- {e} -----#\n")
            continue

    lowest, highest = find_maxmin(numbers)

    print(
        f"\nLowest number: {lowest}\nHighest number: {highest}")


if __name__ == "__main__":
    main()
