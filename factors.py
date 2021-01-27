#!/usr/bin/python3
"""Factors file"""
import sys


def factors():
    """Factorize a number into the 2 smallest factors"""
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        raise(TypeError, "Usage: factors <file>")
    """open the file"""
    with open(sys.argv[1]) as file:
        for line in file:
            try:
                num1 = int(line)
            except:
                raise(TypeError, "There is a word in this file")
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
                print(str(num1) + "=" + str(factor1) + "*" + str(factor2))
factors()
