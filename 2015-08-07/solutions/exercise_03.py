#!/usr/bin/env python3
# coding: utf-8

from random import randint

n_rolls = input("How many rolls would you like? ")

for n in range(int(n_rolls)):
    a, b, c = (randint(1, 6), randint(1, 6), randint(1, 6))
    print("Roll {}: {}, {}, {}".format(n + 1, a, b, c))
