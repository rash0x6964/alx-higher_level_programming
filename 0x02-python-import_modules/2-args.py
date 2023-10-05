#!/usr/bin/python3
import sys
i = 1
sys.argv.pop(0)
l = len(sys.argv)
if __name__ == '__main__':
    if l == 0:
        print('0 arguments.')
    if len(sys.argv) > 0:
        if l == 1:
            print('1 argument:')
        else:
            print('{} arguments:'.format(l))
        for arg in sys.argv:
            print('{}: {}'.format(i, arg))
            i+=1
