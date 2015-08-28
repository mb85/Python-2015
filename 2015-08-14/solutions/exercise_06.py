#!/usr/bin/env python3
# coding: utf-8

import itertools

list1 = ["a", "b", "c", "d", "e", "f"]
list2 = [1, 2, 3, 4, 5, 6]
merged = zip(list1, list2)

print(list(itertools.chain.from_iterable(merged)))
