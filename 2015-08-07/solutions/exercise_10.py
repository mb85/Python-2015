#!/usr/bin/env python3
# coding: utf-8

import random

types = {"r": "Rock", "p": "Paper", "s": "Scissors"}
computer = random.choice(("r", "p", "s"))

while True:
    user = input("Please enter a choice from 'r', 'p' or 's': ").lower()
    if user not in ("r", "p", "s"):
        print("Invalid choice! Please choose 'r', 'p' or 's'.\n")
    else:
        break

print("\nComputer: {}\nPlayer: {}\n".format(types.get(computer), types.get(user)))

wins = (
    ("r", "s"),
    ("p", "r"),
    ("s", "p")
)

if computer == user:
    print("Draw!")
else:
    if (computer, user) in wins:
        print("Computer wins!")
    else:
        print("You win!")
