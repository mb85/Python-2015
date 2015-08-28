#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from collections import Counter


def most_common(path, number=20):
    words = []
    with open(path) as f:
        for line in f:
            words.extend(line.split())

    yield from Counter(words).most_common(number)


def main():
    args = sys.argv[1:]
    if args:
        path = args[0]
        for word, freq in most_common(path):
            print("{}: {}".format(word, freq))

if __name__ == "__main__":
    sys.exit(main())
