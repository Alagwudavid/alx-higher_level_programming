#!/usr/bin/python3
for i in range(0, 98 + 1):
    if i < 99:
        print('{:02d}'.format(i), end=', ')
    else:
        print(i)
