#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    
    return [alice, bob]

if __name__ == '__main__':

    a = list(map(int, input("Enter Alice's scores: ").rstrip().split()))
    b = list(map(int, input("Enter Bob's scores: ").rstrip().split()))

    result = compareTriplets(a, b)

    output_str = ' '.join(map(str, result))

    print("Result:", output_str)