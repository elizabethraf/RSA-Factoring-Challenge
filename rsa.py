#!/usr/bin/env python3
import sys

def is_prime(n):
    """Checks whether a given number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    """Finds the prime factors of a given RSA number n."""
    for i in range(2, n//2+1):
        if n % i == 0 and is_prime(i) and is_prime(n//i):
            return i, n//i

if len(sys.argv) != 2:
    print('Usage: python rsa.py <file>')
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    for line in f:
        n = int(line.strip())
        p, q = find_prime_factors(n)
        print(f"{n} = {p} * {q}")

