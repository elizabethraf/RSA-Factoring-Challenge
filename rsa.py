#!/usr/bin/env python3

import sys
import subprocess

def check_factor(*args):
    if len(args) != 3:
        num2 = 1

    for a in args:
    if isinstance(a, int):
        num2 *= a
        num1 = args[-1]
    else:
        num2 = args[-1]
        num1 = args[-2]

    if num2 > num1:
        num1, num2 = num2, num1

        num_str = f"{args[0]}={args[1]}*"
        return f"{num_str}{num1}*{num2}"

    if len(sys.argv) != 2:
        print('Usage: rsa <file>')
            sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as f:
        for line in f:
            num = int(line.strip())
            result = subprocess.check_output(['factor', str(num)])
            factors = list(map(int, result.decode().strip().split(':')[1].split()))
            print(check_factor(*factors))

