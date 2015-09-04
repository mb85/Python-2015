#!/usr/bin/env python3
# coding: utf-8


def framed(u_input: str, sep: str):
    lines = u_input.split(sep)
    formatted = ""

    longest_line = len(sorted(lines, key=lambda x: len(x))[-1])
    formatted += "*" * (longest_line + 2) + "\n"
    for line in lines:
        formatted += "*{}*\n".format(line.ljust(longest_line))
    formatted += "*" * (longest_line + 2) + "\n"

    return formatted

print(framed("This is|a test for|framing", "|"))
