#!/usr/bin/python3

def search_replace(my_list, search, replace):
    'Write a function that replaces all occurrences of an element by another in a new list.'

    return list(map(lambda x: x if (x != search) else replace, my_list))

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
