#!/usr/bin/python3
import sys
i = 1
sys.argv.pop(0)
length = len(sys.argv)
if __name__ == '__main__':
    if length == 0:
        print('0 arguments.')
    if len(sys.argv) > 0:
        if length == 1:
            print('1 argument:')
        else:
            print('{} arguments:'.format(length))
        for arg in sys.argv:
            print('{}: {}'.format(i, arg))
            i += 1
