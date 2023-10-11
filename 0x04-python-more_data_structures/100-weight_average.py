#!/usr/bin/python3

def weight_average(my_list=[]):
    total_weight = 0
    credit = 0

    for tup in my_list:
        credit += tup[0] * tup[1]
        total_weight += tup[1]
    return credit / total_weight
