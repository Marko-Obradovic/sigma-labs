def num_to_char(numbers: list) -> list[dict[str,str]]:
    """
    Converts a list of numbers (ASCII values) into a list of 
    dictionaries where the key is the number and the value is the
    character the number represents.

    Parameters:
        numbers (list): a list of integers representing ASCII values.

    Returns:
        list: a list of dictionaries, each containing:
            - key (str): the ASCII value.
            - value (str): the character corresponding to the ASCII value.

    Example:
        >>> ascii_to_char_dict([65, 66, 67])
        [{'65': 'A'}, {'66': 'B'}, {'67': 'C'}]
    """

    result = [{str(num): chr(num)} for num in numbers]
    return result

