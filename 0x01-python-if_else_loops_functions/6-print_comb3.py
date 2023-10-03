#!/usr/bin/python3
for n1 in range(0, 9):
    for n2 in range(1, 10):
        if n1 == 8 and n2 == 9:
            print("{}{}".format(n1, n2))
        else:
            print("{}{}".format(n1, n2), end=", ")
