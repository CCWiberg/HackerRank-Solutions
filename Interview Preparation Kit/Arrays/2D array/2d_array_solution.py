
#!/bin/python3

import math
import os
import random
import re
import sys

def sumHourglass(arr, i, j):
    sum = 0
    for n in range(i, i+3):
        for m in range(j, j+3):
            if n == (2*i + 3)//2:
                if m == (2*j + 3)//2:
                    ##print("    ", n, m, end=", ")
                    sum += arr[n][m]
            else:
                ##print(n, m, end=", ")
                sum += arr[n][m]
        ##print("")
    ##print("")
    return sum

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_arr = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum = sumHourglass(arr, i, j)
            sum_arr.append(sum)
    return max(sum_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
