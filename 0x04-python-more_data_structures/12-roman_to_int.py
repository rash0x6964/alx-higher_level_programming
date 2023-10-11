#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    prev_res = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for n in roman_string:
        if roman[n] > prev_res:
            res += roman[n] - 2 * prev_res
        else:
            res += roman[n]
        prev_res = roman[n]
    return res
    
