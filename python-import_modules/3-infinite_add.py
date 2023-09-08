#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    sum = 0
    if args == 1:
        print("0")
    elif args == 2:
        print("{}".format(argv[1]))
    else:
        for i in range(1, args):
            sum += int(argv[i])
            print("{}".format(sum))

