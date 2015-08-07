#!/usr/bin/env python3
# coding: utf-8

sentence = input("Please enter a sentence: ")

vowels = 0

for char in sentence:
    if char in "aeiou":
        vowels += 1

print("There are {} vowels and {} consonants in your sentence.".format(
    vowels, len(sentence) - vowels))
