#!/usr/bin/python3
"""this function finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of numbers"""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = list_of_integers[mid]

        if (mid == 0 or mid_val >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1
                or mid_val >= list_of_integers[mid + 1]):
            return mid_val
        elif mid > 0 and list_of_integers[mid - 1] > mid_val:
            high = mid - 1
        else:
            low = mid + 1

    return None
