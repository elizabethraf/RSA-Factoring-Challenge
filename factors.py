#!/usr/bin/python3
import sys
import math

def factorize(n):
    """
    Given a natural number n, return a tuple (p, q) where p*q = n and p <= q.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (i, n // i)
    return (n, 1)

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file) as f:
    for line in f:
        n = int(line.strip())
        p, q = factorize(n)
        print(f"{n}={p}*{q}")

