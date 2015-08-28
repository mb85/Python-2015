#!/usr/bin/env python3
# coding: utf-8

import sys

args = sys.argv[1:]
if args:
    word = sys.argv[0]
    if len(set(word)) == len(word):
        print("All letters in this word are unique.")
    else:
        print("Not all letters in this word are unique.")
