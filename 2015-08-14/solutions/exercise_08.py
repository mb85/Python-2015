#!/usr/bin/env python3
# coding: utf-8

import sys


def main():
    args = sys.argv[1:]
    if args:
        word = args[0]
        if len(set(word)) == len(word):
            print("All letters in this word are unique.")
        else:
            print("Not all letters in this word are unique.")

if __name__ == "__main__":
    sys.exit(main())
