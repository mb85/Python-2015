#!/usr/bin/env python3
# coding: utf-8

# 1,  2,  3,  4,  5
# 2,  4,  6,  8,  10
# 3,  6,  9,  12, 15
# 4,  8,  12, 16, 20
# 5,  10, 15, 20, 25

size = int(input("How big would you like your times table? "))

for a in range(1, size + 1):
    for b in range(1, size + 1):
        product = a * b
        print("{}\t".format(product), end="")

    print()
