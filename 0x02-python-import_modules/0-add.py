#!/usr/bin/python3
import_add = __import__('add_0').add
sum = import_add(1, 2)
print("1 + 2 = {}".format(sum))
