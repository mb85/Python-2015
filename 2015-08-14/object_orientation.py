#!/usr/bin/env python3
# coding: utf-8

class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        vol = self.length * self.width * self.height
        return vol

box_one = Box(10, 20, 30)
box_two = Box(20, 30, 40)

class ColouredBox(Box):
    def __init__(self, length, width, height, colour):
        super().__init__(length, width, height)
        self.colour = colour

box_one = ColouredBox(10, 20, 30, "Blue")

print(box_one.get_volume())
print(box_one.colour)
