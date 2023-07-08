#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = 0
if number > 0:
    Last_digit = number % 10
elif number < 0:
    Last_digit = ((number * -1) % 10) * -1
if Last_digit > 5:
    msg = 'Last digit of {0} is {1} and is greater than 5'
elif Last_digit < 6 and Last_digit != 0:
    msg = 'Last digit of {0} is {1} and is less than 6 and not 0'
else:
    msg = 'Last digit of {0} is {1} and is 0'
print(msg.format(number, Last_digit))
