#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number % 10)
if Last_digit > 5:
    message = 'Last digit of {0} is {1} and is greater than 5'.format(number, Last_digit)
elif Last_digit < 6 and Last_digit != 0:
    message = 'Last digit of {0} is {1} and is less than 6 and not 0'.format(number, Last_digit)
else:
    massage = 'Last digit of {0} is {1} and is 0'.format(number, Last_digit)
    print(massage)
