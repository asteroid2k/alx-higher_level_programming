#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argz = [int(arg) for arg in argv[1:]]
    print(f"{sum(argz):d}")
