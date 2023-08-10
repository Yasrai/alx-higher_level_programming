#!/usr/bin/python3
for number in range(0, 106):
    if number == 105:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
