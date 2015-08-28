#!/usr/bin/env python3
# coding: utf-8

import sys


def factorial(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


def main():
    args = sys.argv[1:]
    if args:
        n = args[0]
        print(factorial(n))
