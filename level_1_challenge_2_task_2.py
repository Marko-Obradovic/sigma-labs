import random
import string
import styling

while True:
    try:
        username_creation_method = int(
            input(
                '\nWelcome to the username creator... Please choose one of the following options:\n\n1. Create a username based on a name\n2. Generate a random username\n\nType the number you want to select: '
            ))
        break
    except ValueError:
        print(styling.notification('Error - Please enter either 1 or 2!'))


def reverse_name(name_input) -> str:
    char_list = [char for char in name_input]
    char_list.reverse()
    return ''.join(char_list)


def intersperse_name(name_input, surname_input, list_to_append_to) -> None:
    for index, char in enumerate(name_input):
        list_to_append_to.append(char)
        if index < len(surname):
            list_to_append_to.append(surname_input[index])
        if index == len(name_input) - 1:
            for remaining_char in surname_input[index + 1:]:
                list_to_append_to.append(remaining_char)


def random_name_generator(char_list) -> str:
    return ''.join(random.choices(char_list, k=random.randint(3, 9)))


def format_name(char_list) -> str:
    char_list.insert(len(name), ' ')
    return ''.join(char_list).title()


letters = [letter for letter in string.ascii_letters]
numbers = [str(number) for number in range(10)]
letters_and_numbers_list = letters + numbers

interspersed_char_list = []

if username_creation_method == 1:
    name = input('\nName: ').lower()
    surname = input('Surname: ').lower()
    is_random = ''

elif username_creation_method == 2:
    name = random_name_generator(letters_and_numbers_list)
    surname = random_name_generator(letters_and_numbers_list)
    is_random = 'random '

intersperse_name(reverse_name(name), surname, interspersed_char_list)

print(
    f'\nYour {is_random}username is: {format_name(interspersed_char_list)}\n')
