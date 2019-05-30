#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    elevation = 0
    below = False
    valleycount = 0
    for d in s:
        if d == 'U':
            elevation += 1
        elif d == 'D':
            elevation -= 1
        if elevation  < 0:
            below = True
        else:
            if below:
                valleycount += 1
                below = False
        
    return valleycount

            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
