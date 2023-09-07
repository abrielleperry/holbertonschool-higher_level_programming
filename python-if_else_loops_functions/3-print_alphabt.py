#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) == "e" or chr(letter) == "q":
        continue
    else:
        print("{:c}".format(letter), end='')
