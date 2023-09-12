#!/usr/bin/python3
def roman_to_int(roman_string):
    rn_values = {
    'I': 1
    'V': 5
    'X': 10
    'L': 50
    'C': 100
    'D': 500
    'M': 1000
    }
    
    result_int = 0
    previous_val = 0

for numeral in reversed(roman_string):
    value = rn_values.get(numeral, 0)
    if value >= previous_val:
        result_int += value
    else:
        result -= value
