#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = [n for n in my_list]
    if idx >= 0 and idx < len(my_list):
        copy_list[idx] = element
    return copy_list
