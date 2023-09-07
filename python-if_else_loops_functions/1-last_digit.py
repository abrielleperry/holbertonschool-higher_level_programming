#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1:]
print("Last digit of {} is {}".format(number, last), end=' ')
n = str(last)
if int(n) > 5:
    print("and is greater than 5", end=' ')
elif int(n) == 0:
    print("and is 0")
elif int(n) < 6 and int(n) != 0:
    print("and is less than 6 and not 0")
