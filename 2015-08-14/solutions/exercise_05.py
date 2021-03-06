#!/usr/bin/env python3
# coding: utf-8

import sys

key = (
    ("A", ".-"), ("B", "-..."), ("C", "-.-."), ("D", "-.."), ("E", "."), ("F", "..-."),
    ("G", "--."), ("H", "...."), ("I", ".."), ("J", ".---"), ("K", "-.-"), ("L", ".-.."),
    ("M", "--"), ("N", "-."), ("O", "---"), ("P", ".--."), ("Q", "--.-"), ("R", ".-."),
    ("S", "..."), ("T", "-"), ("U", "..-"), ("V", "...-"), ("W", ".--"), ("X", "-..-"),
    ("Y", "-.--"), ("Z", "--.."), ("1", ".----"), ("2", "..---"), ("3", "...--"),
    ("4", "....-"), ("5", "....."), ("6", "-...."), ("7", "--..."), ("8", "---.."),
    ("9", "----."), ("0", "-----"), ("/", "-..-."), ("+", ".-.-."), ("=", "-...-"),
    (".", ".-.-.-"), (",", "--..--"), ("?", "..--.."), ("(", "-.--."), (")", "-.--.-"),
    ("-", "-....-"), ("\"", ".-..-."), ("_", "..--.-"), ("'", ".----."), (":", "---..."),
    (";", "-.-.-."), ("$", "...-..-"), ("=", "-...-")
)


def encode(text):
    d_enc = dict(key)
    encoded = ""
    for c in text.upper():
        encoded += d_enc.get(c, "")
    return encoded


def main():
    args = sys.argv[1:]
    if args:
        print(encode("".join(args)))

if __name__ == "__main__":
    sys.exit(main())
