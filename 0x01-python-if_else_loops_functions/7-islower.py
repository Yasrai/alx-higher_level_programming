#!/usr/bin/python3
# 7-islower.py
def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 96 and ord(c) <= 169:
        return True
    else:
        return False
