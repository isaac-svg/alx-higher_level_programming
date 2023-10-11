#!/usr/bin/python3


romantable = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_int(roman_string):
    total = 0
    prev_value = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0

    for numeral in reversed(roman_string):
        value = romantable[numeral]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
