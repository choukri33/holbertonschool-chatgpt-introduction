#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given number recursively.

    Parameters:
    - n (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)