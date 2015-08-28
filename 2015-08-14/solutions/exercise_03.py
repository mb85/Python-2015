#!/usr/bin/env python3
# coding: utf-8


class Point:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


def distance(p1: Point, p2: Point):
    d = (p1.y - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2
    return d


point_1 = Point()
point_2 = Point()

point_1.x, point_1.y, point_1.z = (float(n) for n in input(
    "Please enter the x, y and z coordinates of the first point: ").split())

point_2.x, point_2.y, point_2.z = (float(n) for n in input(
    "Please enter the x, y and z coordinates of the second point: ").split())

print("The distance between the two points is: {}".format(distance(point_1, point_2)))
