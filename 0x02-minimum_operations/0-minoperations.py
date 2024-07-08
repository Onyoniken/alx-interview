#!/usr/bin/python3

"""Module for 0x02-minimum operations"""

def minOperations(n):
    """
    mmin operations
    """

    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # n evenly divides by root
        if n % root == 0:
            ops += root
            n = n / root # n set to the reminder
            root -= 1 # reduce root to find remaining small val to evenly divide n
            root += 1 # increment root untill it evenly divides n

        return ops
