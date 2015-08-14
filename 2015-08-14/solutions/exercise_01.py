#!/usr/bin/env python3
# coding: utf-8

def factorial(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f

print(factorial(52))

