#!/usr/bin/env python3
# coding: utf-8

n_words = 0

with open("Alice's Adventures in Wonderland.txt") as open_file:
    for line in open_file:
        n_words += len(line.split())

print(n_words)
