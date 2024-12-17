def roman_to_int(s):
    roman_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for i in range(len(s) - 1):
        current_value = roman_to_value[s[i]]
        next_value = roman_to_value[s[i+1]]

        if current_value < next_value:
            total -= current_value
        else:
            total += current_value
    
    last_index_value = roman_to_value[s[-1]]

    return total + last_index_value 
