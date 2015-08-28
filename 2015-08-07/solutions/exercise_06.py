#!/usr/bin/env python3
# coding: utf-8

import sys


def collatz(n: int):
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1

        yield n


def main():
    args = sys.argv[1:]
    if args:
        if args[0].isdigit() and int(args[0]) > 0:
            for n in collatz(int(args[0])):
                print(int(n))

        else:
            print("Please enter a positive integer as input.", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
