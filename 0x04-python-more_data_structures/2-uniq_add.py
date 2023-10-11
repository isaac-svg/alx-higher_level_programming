#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Write a function that adds all unique integers
      in a list (only once for each integer)."""
    # create a cache
    cache = {}
    sum = 0
    for num in my_list:
        if cache.get(num, 0):
            continue
        else:
            cache[num] = num
            sum += num
    return sum
