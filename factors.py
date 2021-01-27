#!/usr/bin/python3
"""Factors file"""
import sys


def factors():
    """Factorize a number into the 2 smallest factors"""
    if len(sys.argv) <= 1:
        raise(TypeError, "Usage: factors [num]")
    if len(sys.argv) > 2:
        raise(TypeError, "Usage: factors [num]")
    num1 = int(sys.argv[1])
    factor1 = 0
    factor2 = 0

    """Start Factoring the number"""
    for a in range(2, num1):
        if num1 % a == 0:
            factor1 = int(num1 / a)
            factor2 = a
            break
    if factor1 == 0 and factor2 == 0:
        print("There are no factors for {}".format(num1))
    else:
        print(factor1, factor2)
factors()
