"""This program takes a number of your choice, either sums or multiplies the numbers 
from 1 to your number - Sums the numbers from 3 to your number in multiples of 3 and 5.
"""

import sys

import functools
from typing import Callable, Any

import styling

def error_handle_get_number_input(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        while True:
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                styling.notification('Program stopped')
                sys.exit()
            except ValueError:
                print(error_message)
    return wrapper

@error_handle_get_number_input
def get_number_input(error_message):
    return int(input('Enter a number: '))


def sum_to_n(end_value_parameter: int) -> int:
    total: int = 0
    for num in range(1, end_value_parameter + 1):
        total += num
    return total


def multiply_to_n(end_value_parameter: int) -> int:
    total: int = 1
    for num in range(1, end_value_parameter + 1):
        total *= num
    return total


def generate_num_sequence(end_value_parameter: int, incrementation:int) -> list:
    return [
        num for num in range(0, end_value_parameter + 1, incrementation)
        if num > 0
    ]


def sum_num_sequences(sequence_one: list[int], sequence_two: list[int]) -> int:
    total: int = 0
    for num in sequence_one + sequence_two:
        total += num
    return total


operator_choice_error = styling.notification('Error. Please enter either 1 or 2')
invalid_number_error = styling.notification('Error. Please enter a valid number')

end_value = get_number_input(error_message=invalid_number_error)

print(styling.line_separator)

def main() -> None:
    print(
        '\nChoose an operation to perform on numbers up to your selected number:\n\n1. Sum the numbers\n2. Multiply the numbers\n'
    )

    while True:
        operator_choice = get_number_input(error_message=operator_choice_error)
        if operator_choice == 1:
            print(styling.line_separator)
            print(
                f'\nNumbers from 1 to {end_value} summed = {sum_to_n(end_value)}\n'
            )
            break
        elif operator_choice == 2:
            print(styling.line_separator)
            print(
                f'\nNumbers from 1 to {end_value} multiplied = {multiply_to_n(end_value)}\n'
            )
            break
        print(operator_choice_error)
 
    multiples_of_three = generate_num_sequence(end_value, incrementation = 3)
    multiples_of_five = generate_num_sequence(end_value, incrementation = 5)

    multiples_of_three_or_five_summed = sum_num_sequences(
            multiples_of_three,
            multiples_of_five
            )

    multiples_of_three_or_five_message = f'Multiples of three or five up to your chosen number summed: {multiples_of_three_or_five_summed}'

    print(multiples_of_three_or_five_message)

if __name__ == "__main__":
    main()
