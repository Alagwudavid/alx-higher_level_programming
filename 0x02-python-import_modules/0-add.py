#!/usr/bin/python3
import_add = __import__('add_0').add
a = 1
b = 2
sum = import_add(a, b)
print("{0} + {1} = {2}".format(a, b, sum))
