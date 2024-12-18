"""This module contains functions to decode messages using a formatted key.
"""

from string import ascii_lowercase

def format_key(key: str) -> dict[str, str]:
    """Removes spaces from a given key and maps unique characters to the alphabet.
    """
    key_removed_spaces: list[str] = [char for char in key if char != " "]

    unique_chars_from_key: list[str] = []

    for char in key_removed_spaces:
        if char not in unique_chars_from_key:
            unique_chars_from_key.append(char)

    key_with_alphabet: dict[str, str] = {
            char:ascii_lowercase[num] for num, char in enumerate(unique_chars_from_key)
            }

    return key_with_alphabet

def decode_message(message: str, formatted_key: dict[str, str]):
    """decode_message: Decodes a message using the formatted key.
    """
    message_decoded: list[str] = []
    for char in message:
        if char == " ":
            message_decoded.append(char)
        else:
            message_decoded.append(formatted_key[char])

    return ''.join(message_decoded)
