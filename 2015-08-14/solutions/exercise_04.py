#!/usr/bin/env python3
# coding: utf-8


def is_automorphic(n):
    if str(n ** 2).endswith(str(n)):
        return True

n_max = int(input("How many automorphic numbers would you like to display? "))
i = 0
n_found = 0

while n_found < n_max:
    if is_automorphic(i):
        print(i)
        n_found += 1

    i += 1
