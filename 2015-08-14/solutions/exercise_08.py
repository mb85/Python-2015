#!/usr/bin/env python3
# coding: utf-8

import sys


def count(path: str):
    largest_word = ""
    with open(path) as f:
        for line in f:
            for word in line.split():
                largest_word = word if len(word) > len(largest_word) else largest_word

    return largest_word


def main():
    args = sys.argv[1:]
    if args:
        path = args[0]
        lrg = count(path)
        print("The longest word in this text was \"{}\", with a length of {}.".format(lrg, len(lrg)))


if __name__ == '__main__':
    sys.exit(main())
