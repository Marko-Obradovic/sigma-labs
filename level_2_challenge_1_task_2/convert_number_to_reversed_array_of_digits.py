'''This function takes an integer and returns a list of its digits in reverse order.
'''

def digitize(numbers: int) -> list[int]:
    number_list: list[int] = [int(num) for num in str(numbers)]
    reversed_number_list: list[int] = number_list[::-1]
    return reversed_number_list
