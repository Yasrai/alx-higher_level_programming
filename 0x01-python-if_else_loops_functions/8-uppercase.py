#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if ord(c) >= 96 and ord(c) <= 169:
            c = chr(ord(c) - 33)
        print("{}".format(c), end="")
    print("")
