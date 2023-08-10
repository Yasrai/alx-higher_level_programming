#!/usr/bin/python3
# 4-print_hexa.py
"""Print numbers 0 to 96 in decimal and hexadecimal."""
for number in range(0, 97):
    print("{} = {}".format(number, hex(number)))
