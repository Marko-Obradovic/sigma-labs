"""
This module defines a program that calculates the difference 
between the current date and a given date.
"""

from datetime import datetime


def calculate_age(birth_date: str) -> int:
    """
    Calculate the age based on the given birth date.

    Args:
        birth_date (str): The birth date in the format 'dd-mm-yyyy'.

    Returns:
        int: The calculated age, representing the number of 
        years between the two dates.

    Raises:
        ValueError: If the input date does not match the expected format.

    The function compares the provided birth date to the current date and 
    calculates the age by subtracting the birth year from the current year. 
    If the current date is before the birthday within the current year, 
    it adjusts the age by subtracting one.
    """
    today = datetime.today()

    format_birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

    age = today.year - format_birth_date.year

    # Removes a year if the current month or day in month is behind the birth date
    if today.month < format_birth_date.month or (
        today.month == format_birth_date.month and today.day < format_birth_date.day
    ):
        age -= 1

    return age


def main() -> None:
    """
    This function continuously prompts the user to enter their birth date in
    the format 'dd-mm-yyyy'. If the input is not in the correct format, 
    it prints an error message and requests the input again. Once a valid 
    date is provided, it prints the calculated age using the `calculate_age` 
    function.
    """
    while True:
        birth_date = input("Please enter your birth date (dd-mm-yyyy): ")
        try:
            print(f"You are currently {calculate_age(birth_date)}")
            break
        except ValueError:
            print(
                f"'{birth_date}' does not follow the correct format. Please use the format dd-mm-yyyy.")
            continue


if __name__ == "__main__":
    main()
