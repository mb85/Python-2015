#!/usr/bin/env python3
# coding: utf-8

import time

x, y = 0, 1

while True:
    print(y)
    x, y = y, x + y
    time.sleep(0.25)
