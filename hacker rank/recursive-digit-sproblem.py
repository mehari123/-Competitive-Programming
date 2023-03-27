#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n):
    # Write your code here
    print(n)
    if int(n) < 10  :
        return int(n)
    n = sum ([int(s) for s in str(n)])
    return superDigit(n)
    # return int(n)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]
    n = sum ([int(s) for s in str(n)])
    k = int(first_multiple_input[1])
    n = n * k
    
    result = superDigit(str(n))

    fptr.write(str(result) + '\n')

    fptr.close()
