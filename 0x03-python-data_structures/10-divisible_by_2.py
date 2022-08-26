#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    multiples = []
    "append True or False in the new list, depening if i is a multiple of 2"
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
