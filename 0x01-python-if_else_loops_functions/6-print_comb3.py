#!/usr/bin/python3
for n1 in range(0, 9):
    for n2 in range(1, 10):
        if n2 > n1 and n1 != 8:
            print("{}{}".format(n1, n2), end=", ")
        elif n1 == 8 and n2 == 9:
            print("{}{}".format(n1, n2))
