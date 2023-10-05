#!/usr/bin/python3
import sys
sys.argv.pop(0)
summ = 0
if __name__ == '__main__':
    for arg in sys.argv:
        summ += int(arg)
    print('{}'.format(summ))
