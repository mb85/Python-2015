#!/usr/bin/env python3
# coding: utf-8

numbers = input("Please enter a string of numbers: ")
total = sum([int(n) for n in numbers])
print("The sum of the numbers entered is: {}.".format(total))
