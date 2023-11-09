#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
	print("Last digit of {} is {} and is greater than 5".format(number, str(number)[-1:]))
elif number == 0:
	print("Last digit of {} is {} and is zero".format(number, str(number)[-1:]))
else number < 6 and number != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, str(number)[-1:]))
