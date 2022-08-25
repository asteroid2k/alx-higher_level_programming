#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argz = argv[1:]
    arg_len = len(argz)
    arg_txt = "argument" if arg_len == 1 else 'arguments'
    arg_end = "." if arg_len < 1 else ':'
    print(f"{arg_len} {arg_txt}{arg_end}")
    for idx, arg in enumerate(argz):
        print(f"{idx + 1}: {arg}")
