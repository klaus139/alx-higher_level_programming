#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    "deletes the items at a specific position in the list"

    "if idx is negative or out of range, nothing change"
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
