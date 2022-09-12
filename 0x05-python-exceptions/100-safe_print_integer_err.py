#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
    finally:
        sys.stderr.write("Exception: {}".format(e))
