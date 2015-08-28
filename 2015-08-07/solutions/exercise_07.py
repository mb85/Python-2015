#!/usr/bin/env python3
# coding: utf-8

import sys
import random


def shuffle(string: str):
    l_string = list(string)
    random.shuffle(l_string)
    return "".join(l_string)


def main():
    args = sys.argv[1:]
    if args:
        print(" ".join((shuffle(word) for word in args)))
        return 0

if __name__ == '__main__':
    sys.exit(main())
