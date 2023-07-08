#!/usr/bin/python3
for e in range(97, 123):
    if e != ord('e') and e != ord('q'):
        print('{:c}'.format(e), end='')
