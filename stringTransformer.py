#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    result = []
    
    for i in range(len(sentence)):
        ch = sentence[i]

        # Case 1: first character of entire sentence
        if i == 0:
            result.append(ch)
            continue

        # Get previous character
        prev = sentence[i - 1]

        # Case 2: if previous char is a space, this is first letter of a word
        if prev == " ":
            result.append(ch)
            continue

        # Compare alphabetically (case-insensitive)
        prev_low = prev.lower()
        ch_low = ch.lower()

        if prev_low < ch_low:
            result.append(ch.upper())
        elif prev_low > ch_low:
            result.append(ch.lower())
        else:
            result.append(ch)

    return "".join(result)
    
    
if __name__ == '__main__':

# SAMPLE INPUT
# a Blue MOON
