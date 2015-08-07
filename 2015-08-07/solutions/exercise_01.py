
#!/usr/bin/env python3
# coding=utf-8

def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False

    return True

n = int(input("Please enter the upper range: "))

for n in range(1, n + 1):
    if is_prime(n):
        print(n)
