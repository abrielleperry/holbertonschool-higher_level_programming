#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("{:d}".format(result))
    except Exception as excep:
        print("{:d}: {}".format(result, e))
        result = None
    finally:
        if result is not None:
            print("{}".format(result))
            return result
