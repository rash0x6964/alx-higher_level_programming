#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    namelist = dir(hidden_4)
    for name in namelist:
        if not name.startswith("__"):
            print('{}'.format(name))
