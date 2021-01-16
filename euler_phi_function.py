#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
from math import gcd

# decoration
print(stylize("\n---- | Get coprimes of n from 1 to n - 1 | ----\n", fg("red")))

# condition
print(stylize("Condition:", fg("green")))
print("Input must be a positive integer.\n")

# user interaction
n = int(input("Define n: "))

# function
def get_coprimes(integer):
    coprimes = []
    for number in range(integer):
        if gcd(integer, number) == 1:
            coprimes.append(number)
    return coprimes, len(coprimes)

# output
output = get_coprimes(n)
print(f"\nCoprimes of {n} are:\n{output[0]}")
print(stylize(f"\nSummarized: {n} has {output[1]} coprimes.\n", fg("red")))
