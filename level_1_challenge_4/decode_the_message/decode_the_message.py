from string import ascii_lowercase
def decode_message(key, message):
    key_removed_spaces = [char for char in key if char != " "]

    key_unique_characters = []

    for char in key_removed_spaces:
        if char not in key_unique_characters:
            key_unique_characters.append(char)

    key_with_alphabet = {char:ascii_lowercase[num] for num, char in enumerate(key_unique_characters)}

    message_decoded = []
    for char in message:
        if char == " ":
            message_decoded.append(char)
        else:
            message_decoded.append(key_with_alphabet[char])

    return ''.join(message_decoded)
