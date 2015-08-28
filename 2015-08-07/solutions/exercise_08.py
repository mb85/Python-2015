#!/usr/bin/env python3
# coding: utf-8

import math


def get_height(distance, angle, height):
    return (math.tan(angle) * distance) + height

d = float(input("How far are you from the base of the tree? "))
a = float(input("What angle is the top of the tree from your eyes? "))
h = float(input("How tall are you? "))


print("The height of the tree is approximately {}.".format(get_height(d, a, h)))

