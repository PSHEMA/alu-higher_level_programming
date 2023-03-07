#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    prev_value = 0

    for roman_char in roman_string:
        curr_value = roman_dict.get(roman_char, 0)
        if curr_value == 0:
            return 0

        if prev_value < curr_value:
            result -= 2 * prev_value

        result += curr_value
        prev_value = curr_value

    return result
