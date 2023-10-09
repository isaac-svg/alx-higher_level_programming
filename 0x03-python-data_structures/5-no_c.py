#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        char = my_string[i]
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
