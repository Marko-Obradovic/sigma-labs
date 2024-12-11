import styling

print(
    '\nThis program does the following:\n\n- Takes a number of your choice\n- Either sums or multiplies the numbers from 1 to your number\n- Sums the numbers from 3 to your number in multiples of 3 and 5.\n'
)


def ask_user_for_number(error_message):
    while True:
        try:
            return int(input('Enter a number: '))
            break
        except ValueError:
            print(error_message)
        except KeyboardInterrupt:
            styling.notification('Program stopped')
            quit()


def sum_to_n(end_value_parameter) -> int:
    total = 0
    for num in range(1, end_value_parameter + 1):
        total += num
    return total


def multiply_to_n(end_value_parameter) -> int:
    total = 1
    for num in range(1, end_value_parameter + 1):
        total *= num
    return total


def generate_num_sequence(end_value_parameter, incrementation) -> list:
    return [
        num for num in range(0, end_value_parameter + 1, incrementation)
        if num > 0
    ]


def sum_num_sequences(sequence_one, sequence_two) -> int:
    total = 0
    for num in sequence_one + sequence_two:
        total += num
    return total


operator_choice_error = styling.notification('Error. Please enter either 1 or 2')
invalid_number_error = styling.notification('Error. Please enter a valid number')

end_value = ask_user_for_number(error_message=invalid_number_error)

print(styling.line_separator)

print(
    '\nChoose an operation to perform on numbers up to your selected number:\n\n1. Sum the numbers\n2. Multiply the numbers\n'
)

while True:
    operator_choice = ask_user_for_number(error_message=operator_choice_error)
    if operator_choice == 1:
        print(styling.line_separator)
        print(
            f'\nNumbers from 1 to {end_value} summed = {sum_to_n(end_value)}\n'
        )
        break
    if operator_choice == 2:
        print(styling.line_separator)
        print(
            f'\nNumbers from 1 to {end_value} multiplied = {multiply_to_n(end_value)}\n'
        )
        break
    else:
        print(operator_choice_error)

print(
    f'Multiples of three or five up to your chosen number summed: {sum_num_sequences(generate_num_sequence(end_value, incrementation = 3), generate_num_sequence(end_value, incrementation = 5))}\n'
)
